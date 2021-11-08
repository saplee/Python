"""Shapes."""
from abc import ABC, abstractmethod
import math
import re


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self.color = color
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.side = side
        self.color = color

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """

        return f'Square (a: {self.side}, color: {self.color})'

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, length: float, width: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.length = length
        self.width = width
        self.color = color

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f'Rectangle (l: {self.length}, w: {self.width}, color: {self.color})'

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.length * self.width


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.my_list = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.my_list.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.my_list

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        return Circle.get_area(circle) + Square.get_area(square)

    def get_circles(self) -> list:
        """Return only circles."""
        result = []
        pattern = r'Circle\w? [(\w: ,]+[)]'
        for word in self.my_list:
            new_word = str(word)
            match = re.search(pattern, new_word)
            if match is not None:
                result.append(word)
        return result

    def get_squares(self) -> list:
        """Return only squares."""
        result = []
        pattern = r'Square\w? [(\w: ,]+[)]'
        for word in self.my_list:
            new_word = str(word)
            match = re.search(pattern, new_word)
            if match is not None:
                result.append(word)
        return result

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        result = []
        pattern = r'Rectangle\w? [(\w: ,]+[)]'
        for word in self.my_list:
            new_word = str(word)
            match = re.search(pattern, new_word)
            if match is not None:
                result.append(word)
        return result


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.get_shapes())
    print(paint.get_circles())
