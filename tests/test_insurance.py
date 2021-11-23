import unittest
import datetime
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
        year = datetime.datetime.now().year - 1
        user = User(29, 1, 'mortgaged', 199999, 'married', [0, 1, 1], year)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.economic.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.economic.name)

    def test_should_apply_for_user_variables_case_1(self):
        year = datetime.datetime.now().year - 1
        user = User(29, 1, 'mortgaged', 199999, 'married', [0, 1, 1], year)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.economic.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.economic.name)

    def test_should_apply_for_user_variables_case_2(self):
        year = datetime.datetime.now().year - 1
        user = User(30, 1, 'mortgaged', 199999, 'married', [0, 1, 1], year)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.economic.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.regular.name)

    def test_should_apply_for_user_variables_case_3(self):
        year = datetime.datetime.now().year - 4
        user = User(35, 1, 'mortgaged', 199999, 'married', [0, 1, 1], year)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.economic.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.regular.name)

    def test_should_apply_for_user_variables_case_4(self):
        year = datetime.datetime.now().year - 4
        user = User(40, 1, 'mortgaged', 199999, 'married', [0, 1, 1], year)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.economic.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.regular.name)

    def test_should_apply_for_user_variables_case_5(self):
        year = datetime.datetime.now().year - 1
        user = User(59, 1, 'mortgaged', 199999, 'married', [0, 1, 1], year)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.regular.name)
        self.assertEqual(score['home'], Score.regular.name)
        self.assertEqual(score['auto'], Score.regular.name)
        self.assertEqual(score['life'], Score.regular.name)

    def test_should_apply_for_user_variables_case_6(self):
        user = User(59, 1, 'owned', 2000001, 'married', [0, 1, 1], 1999)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.economic.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.regular.name)

    def test_should_apply_for_user_variables_case_7(self):
        user = User(59, 1, 'owned', 199999, 'single', [0, 1, 1], 1999)
        insurance = Insurance(user)
        score = insurance.get_risk_score()
        self.assertEqual(score['disability'], Score.regular.name)
        self.assertEqual(score['home'], Score.economic.name)
        self.assertEqual(score['auto'], Score.economic.name)
        self.assertEqual(score['life'], Score.regular.name)