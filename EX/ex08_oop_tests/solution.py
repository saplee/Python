"""Solution."""


class Factory:
    """"init."""

    def __init__(self):
        self.basic = 0
        self.medium = 0
        self.large = 0
        self.amount = 0

    def bake_cake(self, toppings: int, base: int) -> int:
        """Calculating cake size."""
        if toppings == base:
            self.large = base // 5
            self.medium = (base % 5) // 2
            self.basic = ((base % 5) % 2) // 1
            amount = (base // 5) + ((base % 5) // 2) + (((base % 5) % 2) // 1)
            self.amount = amount
        return self.amount


class Cake:

    def __init__(self, base_amount, toppings_amount):
        """Init."""
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount
        self.cake_size = ""

    @property
    def type(self):
        """Cake size."""
        if self.base_amount == 1 and self.toppings_amount == 1:
            self.cake_size = "basic"
        if self.base_amount == 2 and self.toppings_amount == 2:
            self.cake_size = "medium"
        if self.base_amount == 5 and self.toppings_amount == 5:
            self.cake_size = "large"
        return self.cake_size
