import uuid
from datetime import date
from itertools import chain
from typing import List

from pydantic import Field

from finstruments.common.base import Base
from finstruments.common.decorators import serializable
from finstruments.instrument import BaseInstrument


@serializable
class Position(Base):
    """
    A position is composed of instrument and size.
    """

    instrument: BaseInstrument
    size: float
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))


@serializable
class Trade(Base):
    """
    A trade, which could involve a number of instruments. For example, as straddle could be managed as a single unit,
    but it is composed of a call and a put.
    """

    positions: List[Position] = Field(default_factory=lambda: [])

    def get_expired_positions(self, as_of_date: date) -> List[Position]:
        return [
            x
            for x in self.positions
            if (x.instrument.pillar_date is not None)
            and x.instrument.pillar_date <= as_of_date
        ]

    def filter_expired_positions(self, as_of_date: date) -> "Trade":
        positions = [
            x
            for x in self.positions
            if (x.instrument.pillar_date is None)
            or (x.instrument.pillar_date > as_of_date)
        ]

        return Trade(positions=positions)

    def filter_positions(self, ids: List[str]) -> "Trade":
        positions = [x for x in self.positions if not (x.id in ids)]

        return Trade(positions=positions)


@serializable
class Portfolio(Base):
    """
    A list of trades. For example, multiple straddles.
    """

    trades: List[Trade] = Field(default_factory=lambda: [])

    def __sub__(self, other) -> List[Position]:
        return list(set(self.positions) - set(other.positions))

    def get_expired_positions(self, as_of_date: date) -> List[Position]:
        return [
            x
            for x in self.positions
            if (x.instrument.pillar_date is not None)
            and x.instrument.pillar_date <= as_of_date
        ]

    def filter_expired_positions(self, as_of_date: date) -> "Portfolio":
        trades = [trade.filter_expired_positions(as_of_date) for trade in self.trades]

        return Portfolio(trades=trades)

    def filter_positions(self, ids: List[str]) -> "Portfolio":
        trades = [trade.filter_positions(ids) for trade in self.trades]
        # filter out empty trades
        filtered_trades = [trade for trade in trades if len(trade.positions) > 0]

        return Portfolio(trades=filtered_trades)

    @property
    def positions(self) -> List[Position]:
        trade_positions: List[List[Position]] = [x.positions for x in self.trades]
        positions: List[Position] = list(chain(*trade_positions))

        return positions

    def add_trade(self, trade: Trade) -> "Portfolio":
        return Portfolio(trades=self.trades + [trade])

    def add_position(self, position: Position) -> "Portfolio":
        return Portfolio(trades=self.trades + [Trade(positions=[position])])
