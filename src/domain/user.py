import datetime


class User:

    def __init__(self, age, dependents, ownership_status, income, marital_status, risk_questions, vehicle_year):
        self.age = age
        self.dependents = dependents
        self.house = None if ownership_status is None else House(ownership_status)
        self.income = income
        self.marital_status = marital_status
        self.risk_questions = risk_questions
        self.vehicle = None if vehicle_year is None else Vehicle(vehicle_year)

    def is_married(self):
        return self.marital_status == 'married'


class Vehicle:

    def __init__(self, vehicle_year):
        self.vehicle_year = vehicle_year

    def is_less_than(self, number):
        now = datetime.datetime.now()
        return (now.year - self.vehicle_year) < number


class House:

    def __init__(self, ownership_status):
        self.ownership_status = ownership_status

    def is_mortgaged(self):
        return self.ownership_status == 'mortgaged'