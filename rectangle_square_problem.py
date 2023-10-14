class Rectangle:
    def __init__(self, width: float, height: float):
        self._set_width(width)
        self._set_height(height)

    def _set_width(self, value: float):
        self._width: float = value

    def _set_height(self, value: float):
        self._height: float = value

    def perimetr(self) -> float:
        return 2 * self._height + 2 * self._width

    def area(self) -> float:
        return self._width * self._height


class Square(Rectangle):
    def _set_height(self, value: float):
        self._width = value
        self._height = value

    def _set_width(self, value: float):
        self._width = value
        self._height = value


def calculate_shape_area(shape: Rectangle):
    print(f"Shape {type(shape).__name__} {shape._width}x{shape._height} area: {shape.area()}")


rectangle = Rectangle(2, 5)
calculate_shape_area(rectangle)

square = Square(2, 5)
calculate_shape_area(square)
