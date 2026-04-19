class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value

    def set_height(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value

    def get_area(self) -> float:
        return self._width * self.set_height

    def get_perimeter(self) -> float:
        return 2 * (self._width * self._height)

    def get_diagonal():
        pass

    def get_picture():
        pass

    def get_amount_inside():
        pass
