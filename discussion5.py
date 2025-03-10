# 1. Write a Python class to reverse a string word by word.
# Example:
# Input string : 'hello .py'
# Expected Output : '.py hello'

import math

class StringReverser:
    def reverse_words(str):
        return ' '.join(str.split()[::-1])

input_string = 'hello .py'
reversed_string = StringReverser.reverse_words(input_string)
print("Reversed String: ", reversed_string)

input_string2 = 'This is a whole sentence. Testing to see if the class function can handle reversing this.'
reversed_string2 = StringReverser.reverse_words(input_string2)
print("Reversed String2: ", reversed_string2)

#2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
