import unittest
from datetime import date

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import EuropeanExerciseStyle
from finstruments.instrument.common.option.payoff import VanillaPayoff, OptionType
from finstruments.instrument.equity import CommonStock
from finstruments.instrument.equity import EquityOption
from finstruments.portfolio import Position, Trade, Portfolio


class PortfolioTest(unittest.TestCase):
    def test_trade_get_expired_positions_empty(self):
        trade = Trade(positions=[])

        d = date(2022, 1, 1)

        self.assertListEqual(trade.get_expired_positions(d), [])

    def test_trade_get_expired_positions(self):
        d = date(2022, 1, 1)

        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )
        trade = Trade(positions=[equity, option])

        self.assertListEqual(trade.get_expired_positions(d), [option])

    def test_trade_filter_expired_positions_empty(self):
        trade = Trade(positions=[])

        d = date(2022, 1, 1)

        self.assertEqual(trade.filter_expired_positions(d), trade)

    def test_trade_filter_expired_positions(self):
        d = date(2022, 1, 1)

        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )

        option2 = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(
                    expiration_date=date(2023, 1, 1), cut=NysePMCut()
                ),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )
        trade = Trade(positions=[equity, option, option2])

        self.assertEqual(
            trade.filter_expired_positions(d), Trade(positions=[equity, option2])
        )

    def test_trade_filter_positions(self):
        empty_trade = Trade(positions=[])
        self.assertEqual(empty_trade.filter_positions(["test", "test2"]), empty_trade)

        trade = Trade(
            positions=[
                Position(size=1, instrument=CommonStock(ticker="AAPL")),
                Position(size=1, instrument=CommonStock(ticker="AAPL")),
                Position(size=1, instrument=CommonStock(ticker="AAPL")),
            ]
        )

        self.assertEqual(trade.filter_positions(["test"]), trade)
        self.assertEqual(
            trade.filter_positions([p.id for p in trade.positions]), Trade()
        )
        self.assertEqual(
            trade.filter_positions([trade.positions[0].id]),
            Trade(positions=trade.positions[1:3]),
        )

    def test_portfolio_filter_positions(self):
        empty_portfolio = Portfolio(trades=[])
        self.assertEqual(
            empty_portfolio.filter_positions(["test", "test2"]), empty_portfolio
        )

        trade = Trade(
            positions=[
                Position(size=1, instrument=CommonStock(ticker="AAPL")),
                Position(size=1, instrument=CommonStock(ticker="AAPL")),
                Position(size=1, instrument=CommonStock(ticker="AAPL")),
            ]
        )
        portfolio = Portfolio(trades=[trade])

        self.assertEqual(portfolio.filter_positions(["test"]), portfolio)
        self.assertEqual(
            portfolio.filter_positions([p.id for p in trade.positions]), Portfolio()
        )
        self.assertEqual(
            portfolio.filter_positions([trade.positions[0].id]),
            Portfolio(trades=[Trade(positions=trade.positions[1:3])]),
        )

    def test_portfolio_get_expired_positions(self):
        d = date(2022, 1, 1)

        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )

        option2 = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(
                    expiration_date=date(2023, 1, 1), cut=NysePMCut()
                ),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )
        trade = Trade(positions=[equity, option, option2])
        portfolio = Portfolio(trades=[trade])

        self.assertListEqual(portfolio.get_expired_positions(d), [option])

    def test_portfolio_filter_expired_positions(self):
        d = date(2022, 1, 1)

        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )

        option2 = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(
                    expiration_date=date(2023, 1, 1), cut=NysePMCut()
                ),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )
        trade = Trade(positions=[equity, option, option2])
        portfolio = Portfolio(trades=[trade])

        self.assertEqual(
            portfolio.filter_expired_positions(d),
            Portfolio(trades=[Trade(positions=[equity, option2])]),
        )

    def test_portfolio_get_positions(self):
        d = date(2022, 1, 1)
        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )

        option2 = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(
                    expiration_date=date(2023, 1, 1), cut=NysePMCut()
                ),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )
        portfolio = Portfolio(
            trades=[Trade(positions=[equity]), Trade(positions=[option, option2])]
        )

        self.assertListEqual(portfolio.positions, [equity, option, option2])

    def test_portfolio_add_trade(self):
        d = date(2022, 1, 1)
        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )

        option2 = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(
                    expiration_date=date(2023, 1, 1), cut=NysePMCut()
                ),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )
        portfolio = Portfolio(trades=[Trade(positions=[equity])])

        new_portfolio = portfolio.add_trade(Trade(positions=[option, option2]))

        self.assertEqual(
            Portfolio(
                trades=[Trade(positions=[equity]), Trade(positions=[option, option2])]
            ),
            new_portfolio,
        )

    def test_portfolio_add_position(self):
        d = date(2022, 1, 1)
        equity = Position(instrument=CommonStock(ticker="TEST"), size=0)

        option = Position(
            instrument=EquityOption(
                underlying=CommonStock(ticker="TEST"),
                payoff=VanillaPayoff(option_type=OptionType.CALL, strike_price=100),
                exercise_type=EuropeanExerciseStyle(expiration_date=d, cut=NysePMCut()),
                denomination_currency=Currency.USD,
                contract_size=100,
            ),
            size=0,
        )

        portfolio = Portfolio(trades=[Trade(positions=[equity])])

        new_portfolio = portfolio.add_position(option)

        self.assertEqual(
            Portfolio(trades=[Trade(positions=[equity]), Trade(positions=[option])]),
            new_portfolio,
        )
