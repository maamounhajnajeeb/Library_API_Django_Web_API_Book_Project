class Record:
    """
    Hold a record of data.
    """

john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

record_obj = Record()

for key, value in john.items():
    setattr(record_obj, key, value)
print(vars(record_obj))

###################################
class User:
    pass

user = User()
user.name = "Maamoun"
user.age = 23

def __init__(self, name, age):
    self.name, self.age = name, age

User.__init__ = __init__

user = User("Ahmad", 13)
print(user.name)

###################################
import math 

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("Positive integer expected")
        self._radius = value
    
    def calculate_area(self):
        return round(self.radius * math.pi ** 2, 2)

circle_1 = Circle(100) # going directly to setter method
# circle_1 = Circle(-100) # error
print(circle_1.radius)
circle_1.radius = 500

########################################################
# class Square:
#     def __init__(self, side):
#         self.side = side

#     @property
#     def side(self):
#         return self._side

#     @side.setter
#     def side(self, value):
#         if not isinstance(value, int | float) or value <= 0:
#             raise ValueError("positive number expected")
#         self._side = value

#     def calculate_area(self):
#         return round(self._side**2, 2)
# s= Square(5)


#########################################

class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value

class Circle:
    blank = PositiveNumber()

    def __init__(self, radius):
        self.blank = radius

    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)

class Square:
    side = PositiveNumber()

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return round(self.side**2, 2)
    
circle = Circle(100)
print(circle.blank)
print(vars(circle))

circle.radius = 500
print(circle.radius)


#####################
# class Rand:
#     __slots__ = ("x", "y")
    
#     def __init__(self, x, y) -> None:
#         self.x, self.y = x, y
    
#     def returning_point(self):
#         return (self.x, self.y)

# r = Rand(4,5)

# def reveresed_point(self):
#     return self.y, self.x 

# Rand.reveresed_point = reveresed_point

# print(r.returning_point())
# print(r.reveresed_point())

##########################################

# class ThreeDPoint:
#     def __init__(self, x, y, z) -> None:
#         self.x, self.y, self.z = x, y, z
#     def __iter__(self):
#         for x in {self.x, self.y, self.z}:
#             yield x

# tdp = ThreeDPoint(4, 5, 6)
# print(list(tdp))

##########################################

# class ThreeDPoint:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __iter__(self):
#         yield from (self.x, self.y, self.z)

#     @classmethod
#     def from_sequence(cls, sequence):
#         return cls(*sequence)
    
#     def static_func(*args):
#         return [i for i in args]
    
#     def __repr__(self) -> str:
#         return f"{self.x}, {self.y}, {self.z}"

# seq = 1, 2, 3
# TDPo = ThreeDPoint.from_sequence((seq))
# print(TDPo)
# print(ThreeDPoint.static_func(8, 7, 4))

##########################################
# from dataclasses import dataclass

# @dataclass
# class ThreeDPoint:
#     x: int | float
#     y: int | float
#     z: int | float
    
#     @classmethod
#     def from_sequence(cls, *sequence):
#         return cls(*sequence)
    
#     @staticmethod
#     def show_intro_message(name):
#         print(f"Hey {name}! This is your 3D Point!")

# point = ThreeDPoint.from_sequence(1, 2, 3)
# print(point)

# point = ThreeDPoint(1, 2, 3)
# print(point)

##########################################

