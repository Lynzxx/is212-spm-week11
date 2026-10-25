class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area().")

    def calculate_area(self, shape_type, **kwargs):
        shape_class = SHAPES.get(shape_type)
        if shape_class is None:
            return None
        return shape_class(**kwargs).area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


SHAPES = {
    'circle': Circle,
    'rectangle': Rectangle,
    'triangle': Triangle,
}
