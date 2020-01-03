class Person:
    def setName(self,na,ag):
        self.name=na
        self.age=ag
    def display(self):
        print("name:",self.name)
        print("age:",self.age)

ob=Person()
ob.setName("geeth",16)
ob.display()
ob1=Person()
ob1.setName("bee",34)
ob1.display()
print(ob.name)
print(ob1.age)