class Insurance:

    def __init__(self, user):
        self.disability_points = 0
        self.auto_points = 0
        self.home_insurance_points = 0
        self.life_points = 0
        self.disability = None
        self.life = None
        self.home_insurance = None
        self.auto = None
        self.__apply_rules__(user)

    def __apply_rules__(self, user):
        self.__apply_over_than_sixty(user)
        self.__apply_under_third_years(user)
        self.__apply_between_forty_and_third(user)
        self.__apply_between_forty_and_third(user)
        self.__apply_income_above_than_200(user)
        self.__apply_house_is_mortgaged__(user)
        self.__apply_is_married__(user)
        self.__apply_has_dependencies__(user)
        self.__apply_vehicle_five_last_years__(user)


    def __apply_over_than_sixty(self, user):
        if user.age > 60:
            self.disability = 'ineligible'
            self.life = 'ineligible'


    def __apply_under_third_years(self, user):
        if user.age < 30:
            self.disability_points = -2
            self.auto_points = -2
            self.home_insurance_points = -2
            self.life_points = -2

    def __apply_between_forty_and_third(self, user):
        if 30 < user.age < 40:
            self.disability_points = -1
            self.auto_points = -1
            self.home_insurance_points = -1
            self.life_points = -1

    def __apply_income_above_than_200(self, user):
        if user.income > 200000:
            self.disability_points = -1
            self.auto_points = -1
            self.home_insurance_points = -1
            self.life_points = -1

    def __apply_house_is_mortgaged__(self, user):
        if user.house.is_mortgaged():
            self.disability_points = 1
            self.home_insurance_points = 1

    def __apply_has_dependencies__(self, user):
        if user.house.is_mortgaged():
            self.disability_points = 1
            self.life_points = 1

    def __apply_is_married__(self, user):
        if user.is_married():
            self.disability_points = -1
            self.life_points = 1

    def __apply_vehicle_five_last_years__(self, user):
        if user.vehicle.is_less_than(5):
            self.auto_points = 1

    def get_risk_score(self):
        return {
            'auto': self. __get_auto__(),
            'disability': self.__get_disability__(),
            'home': self.__get_home__(),
            'life': self.__get_life__()
        }

    def __get_disability__(self):
        if self.disability is not None:
            return self.disability

        return self.__get_score__(self.disability_points)

    def __get_auto__(self):
        if self.auto is not None:
            return self.auto

        return self.__get_score__(self.auto_points)

    def __get_home__(self):
        if self.home_insurance is not None:
            return self.home_insurance

        return self.__get_score__(self.home_insurance_points)

    def __get_life__(self):
        if self.life is not None:
            return self.life

        return self.__get_score__(self.life_points)


    def __get_score__(self, number):
        if number < 0:
            return 'economic'
        elif number > 1 and number < 2:
            return 'regular'
        else:
            return 'responsible'





