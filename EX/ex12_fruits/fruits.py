"""Fruits delivery application."""


class Product:
    """Product class."""

    def __init__(self, name, price):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price


class Order:
    """Order class."""

    def __init__(self, customer=None):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.customer = customer
        self.result = {}

    def get_customer(self):
        """Return customer."""
        return self.customer

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
        if product[0] not in self.result:
            self.result[product[0]] = int(product[1])
        else:
            self.result[product[0]] += int(product[1])

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        for word in products:
            if word[0] not in self.result:
                self.result[word[0]] = int(word[1])
            else:
                self.result[word[0]] += int(word[1])

    def get_products(self):
        """"Method return dict."""
        return self.result


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.order_list = self.import_products("pricelist.txt")
        self.customers = []
        self.order = []
        self.orders = []

    def find_product_by_name(self, name: str):
        """Find product by name."""
        for product in self.order_list:
            if product.name == name:
                return product

    def get_products(self) -> list:
        """Getter for products list."""
        return self.order_list

    def import_products(self, filename) -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        order_list = []
        with open(filename) as f:
            for row in f:
                new_row = row.split(" - ")
                name = new_row[0].strip()
                price = float(new_row[1].strip())
                order_list.append(Product(name, price))
            return order_list

    def order_products(self, list_of_products: list):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        """
        for number in range(0, len(list_of_products), 2):
            self.order.append(Order(list_of_products[number]))
        self.orders.append(self.order)
        return self.orders

    def get_orders(self) -> list:
        """Getter for orders list."""
        return self.order

    def order(self):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        pass

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.customers.append(customer)

    def add_customers(self, customers):
        """Method for adding several customers to the list."""
        for customer in customers:
            self.customers.append(customer)

    def get_customers(self):
        """Customer list."""
        return self.customers

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

    def __init__(self, name, address):
        """Customer class."""
        self.name = name
        self.address = address
        self.orders = []

    def get_name(self):
        """Get name."""
        return self.name

    def get_address(self):
        """Get address."""
        return self.address

    def get_orders(self):
        """Get orders."""
        return self.orders

    def add_new_order(self, order):
        """Add order to list."""
        self.orders.append(order)
