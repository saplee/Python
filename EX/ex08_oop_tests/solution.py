class Factory:
    def __init__(self):
        self.basic = 0
        self.medium = 0
        self.large = 0

    def bake_cake(self, toppings: int, base: int) -> int:
        amount=0


    def get_last_cakes(self, n: int) -> list:
        pass

    def get_cakes_baked(self) -> list:
        pass

    def __str__(self):
        pass


class Cake:

    def __init__(self, base_amount, toppings_amount):
        pass

    @property
    def type(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


class WrongIngredientsAmountException(Exception):
    pass

