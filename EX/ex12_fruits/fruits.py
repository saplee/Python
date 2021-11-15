"""Fruits delivery application."""
import csv


class Product:
    """Product class."""

    def __init__(self, name, price):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price

    def find_product_by_name(self):
        return self.name


class Order:
    """Order class."""

    def __init__(self):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        product_dict = {}

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """

    def add_product(self, product):
        """Method for adding a single product to the dictionary."""

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        pass


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.my_list = []

    def get_products(self) -> list:
        """Getter for products list."""
        my_list = []
        with open("pricelist.txt") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='-')
            for row in csv_reader:
                word = row[0], row[1]
                name = word.find_product_by_name
                my_list.append(name)
            return my_list

    def get_orders(self) -> list:
        """Getter for orders list."""
        pass

    def import_products(self) -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        self.my_list = []
        with open("pricelist.txt") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='-')
            for row in csv_reader:
                name = row[0]
                price = row[1]
                self.my_list.append(Product(name, price))
            return self.my_list

    def order_products(self):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        """
        pass

    def order(self):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        pass

    def add_customer(self):
        """Method for adding a customer to the list."""
        pass

    def add_customers(self):
        """Method for adding several customers to the list."""
        pass

    def show_all_orders(self) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        pass

    def calculate_total(self) -> float:
        """Method for calculating total price for all customer's orders."""
        pass

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        pass


class Customer:
    """Customer to implement."""

    pass
