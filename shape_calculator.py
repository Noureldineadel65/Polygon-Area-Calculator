class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def __ClassName(cls):
        return cls.__name__

    def __repr__(self):
        return f'{self.__ClassName()}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5



    def get_picture(self):
        if not self.width > 50 or not self.height > 50:
            shape = ""
            for i in range(self.height):
                for n in range(self.width):
                    shape += "*  "
                shape += "\n"
            return shape
        else:
            raise Exception("Can't print a polygon with width or height over 50.")

    def get_amount_inside(self, obj):
        obj_width = obj.width
        obj_height = obj.height
        return self.get_area() // (obj_width * obj_height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def get_perimeter(self):
        return self.width + self.height

    def set_side(self, side):
        self.width = side
        self.height = side

    @classmethod
    def __ClassName(cls):
        return cls.__name__

    def __repr__(self):
        return f'{self.__ClassName()}(side={self.width})'
