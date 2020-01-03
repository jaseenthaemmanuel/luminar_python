#method overriding
class Parent:
    def phone(self):
        print("i have redmi")

class Child(Parent):
    def phone(self):
        print("i have samsung")
c=Child()
c.phone()