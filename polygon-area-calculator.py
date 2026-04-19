from math import sqrt


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"

    def set_width(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value

    def set_height(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value

    def get_area(self) -> float:
        return self._width * self._height

    def get_perimeter(self) -> float:
        return 2 * (self._width * self._height)

    def get_diagonal(self) -> float:
        return sqrt((self._width**2) + (self._height**2))

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        else:
            result = ""
            for i in range(self._height):
                for j in range(self._width):
                    result += "*"
                result += "\n"
            return result

    def get_amount_inside():
        pass
