import unittest

from src.domain.insurance import Insurance
from src.domain.user import User
from src.domain.score import Score


class Insurance_Test(unittest.TestCase):

    def test_should_ineligible_over_than_sixty_years_old(self):
        user = User(61, 2, 'owned', 2000, 'married', [0, 1, 1], 2009)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.ineligible.name)
        self.assertEqual(score['life'], Score.ineligible.name)

    def test_should_ineligible_over_than_sixty_years_old(self):
        user = User(30, 2, None, 0, 'married', [0, 1, 1], None)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.ineligible.name)
        self.assertEqual(score['home'], Score.ineligible.name)
        self.assertEqual(score['auto'], Score.ineligible.name)

    def test_should_apply_for_user_variable(self):
        user = User(29, 2, 'mortgaged', 200001, 'married', [0, 1, 1], 2020)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.ineligible.name)
        self.assertEqual(score['home'], Score.ineligible.name)
        self.assertEqual(score['auto'], Score.regular.name)
        self.assertEqual(score['life'], Score.ineligible.name)