import unittest

from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import VanillaPayoff, DigitalPayoff


class PayoffTest(unittest.TestCase):
    def test_vanilla_payoff(self):
        call_payoff = VanillaPayoff(option_type=OptionType.CALL, strike_price=100)
        put_payoff = VanillaPayoff(option_type=OptionType.PUT, strike_price=100)

        self.assertEqual(call_payoff.compute_payoff(99), 0)
        self.assertEqual(call_payoff.compute_payoff(106), 6)
        self.assertEqual(put_payoff.compute_payoff(99), 1)
        self.assertEqual(put_payoff.compute_payoff(106), 0)

    def test_digital_payoff(self):
        call_payoff = DigitalPayoff(
            option_type=OptionType.CALL, strike_price=100, cash_payout=20
        )
        put_payoff = DigitalPayoff(
            option_type=OptionType.PUT, strike_price=100, cash_payout=20
        )

        self.assertEqual(call_payoff.compute_payoff(99), 0)
        self.assertEqual(call_payoff.compute_payoff(106), 20)
        self.assertEqual(put_payoff.compute_payoff(99), 20)
        self.assertEqual(put_payoff.compute_payoff(106), 0)
