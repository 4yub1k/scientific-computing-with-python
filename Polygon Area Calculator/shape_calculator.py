class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return f"{('*' * self.width)}\n" * self.height

    def get_amount_inside(self, instance):
        return int(self.get_area() / instance.get_area())

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length=0):
        self.side_length = side_length
        super().__init__(self.side_length, self.side_length)

    def set_side(self, side_length=0):
        self.__init__(side_length)

    def set_width(self, width):
        self.side_length = width

    def set_height(self, height):
        self.side_length = height

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.side_length})"
