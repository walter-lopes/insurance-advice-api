import unittest
import datetime
from src.domain.user import User, Vehicle, House
import datetime

class UserTest(unittest.TestCase):

    def test_should_init_user(self):
        user = User(61, 2, 'owned', 2000, 'married', [0, 1, 1], 2009)
        self.assertEqual(user.age, 61)
        self.assertEqual(user.dependents, 2)
        self.assertEqual(user.house.ownership_status, 'owned')
        self.assertEqual(user.income, 2000)
        self.assertEqual(user.marital_status, 'married')
        self.assertEqual(user.risk_questions, [0, 1, 1])
        self.assertEqual(user.vehicle.vehicle_year, 2009)

    def test_vehicle_year_less_than_five(self):
        year = datetime.datetime.now().year - 1
        vehicle = Vehicle(year)
        less_than_5 = vehicle.is_less_than(5)
        self.assertEqual(less_than_5, True)

    def test_vehicle_year_greater_than_five(self):
        year = datetime.datetime.now().year - 10
        vehicle = Vehicle(year)
        greater_than_5 = vehicle.is_less_than(5)
        self.assertEqual(greater_than_5, False)

    def test_house_is_mortgaged(self):
        house = House('mortgaged')
        is_mortgage = house.is_mortgaged()
        self.assertEqual(is_mortgage, True)

    def test_house_is_not_mortgaged(self):
        house = House('owned')
        is_mortgage = house.is_mortgaged()
        self.assertEqual(is_mortgage, False)
