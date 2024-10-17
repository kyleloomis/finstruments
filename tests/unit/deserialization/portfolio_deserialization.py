import unittest
from datetime import date
from finstruments.portfolio import Portfolio, Position, Trade

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NyseAMCut, NysePMCut
from finstruments.instrument.common.exercise_style import (
    BermudanExerciseStyle,
    EuropeanExerciseStyle,
)
from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import DigitalPayoff, VanillaPayoff
from finstruments.instrument.equity import EquityETF, CommonStock
from finstruments.instrument.equity import EquityForward
from finstruments.instrument.equity import EquityFuture
from finstruments.instrument.equity import EquityOption
from tests.unit.deserialization.util import assert_serialization


class TestPortfolioDeserialization(unittest.TestCase):
    def test_base_serialization(self):
        expected = Portfolio(
            trades=[
                Trade(
                    positions=[
                        Position(
                            instrument=EquityOption(
                                underlying=CommonStock(ticker="TEST"),
                                payoff=VanillaPayoff(
                                    option_type=OptionType.CALL, strike_price=100
                                ),
                                exercise_type=EuropeanExerciseStyle(
                                    expiration_date=date(2022, 6, 1), cut=NysePMCut()
                                ),
                                denomination_currency=Currency.USD,
                                contract_size=100,
                            ),
                            size=100,
                        ),
                        Position(
                            instrument=EquityOption(
                                underlying=EquityETF(ticker="TEST"),
                                payoff=DigitalPayoff(
                                    option_type=OptionType.CALL,
                                    strike_price=100,
                                    cash_payout=20,
                                ),
                                exercise_type=BermudanExerciseStyle(
                                    expiration_date=date(2022, 6, 1),
                                    early_exercise_dates=[
                                        date(2022, 1, 1),
                                        date(2022, 3, 1),
                                    ],
                                    cut=NyseAMCut(),
                                ),
                                denomination_currency=Currency.USD,
                                contract_size=100,
                            ),
                            size=5,
                        ),
                    ]
                )
            ]
        )
        expected_two = Portfolio(
            trades=[
                Trade(
                    positions=[
                        Position(
                            instrument=EquityForward(
                                underlying=CommonStock(ticker="TEST"),
                                exercise_type=EuropeanExerciseStyle(
                                    expiration_date=date(2022, 6, 1), cut=NysePMCut()
                                ),
                                strike_price=100,
                                denomination_currency=Currency.USD,
                                contract_size=100,
                            ),
                            size=100,
                        ),
                        Position(
                            instrument=EquityFuture(
                                underlying=EquityETF(ticker="TEST"),
                                exercise_type=EuropeanExerciseStyle(
                                    expiration_date=date(2022, 6, 1), cut=NysePMCut()
                                ),
                                strike_price=100,
                                denomination_currency=Currency.USD,
                                contract_size=100,
                            ),
                            size=5,
                        ),
                    ]
                )
            ]
        )
        assert_serialization(expected, Portfolio)
        assert_serialization(expected_two, Portfolio)

    def test_simple_portfolio(self):
        stock = CommonStock(ticker="AAPL")
        stock_position = Position(instrument=stock, size=100)
        trade = Trade(positions=[stock_position])
        expected = Portfolio(trades=[trade])

        assert_serialization(expected, Portfolio)

    def test_instrument_annotation_update(self):
        expected = Portfolio(
            trades=[
                Trade(
                    positions=[
                        Position(instrument=CommonStock(ticker="TEST"), size=100)
                    ]
                )
            ]
        )
        assert_serialization(expected, Portfolio)
