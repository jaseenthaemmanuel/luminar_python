#operator overloading
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __sub__(self, other):
        return Book(self.pages-other.pages)
    def __mul__(self, other):
        return Book(self.pages*other.pages)
    def __truediv__(self, other):
        return Book(self.pages/other.pages)
    def __str__(self):
        return str(self.pages)

b1=Book(5)
b2=Book(4)
b3=Book(3)
b4=Book(2)
b5=Book(1)
print("object addition")
print(b1+b2+b3+b4+b5)
print("object subtraction")
print(b1-b4-b5)
print("object multiplication")
print(b1*b2*b3*b4*b5)
print("object division")
print(b2/b4)