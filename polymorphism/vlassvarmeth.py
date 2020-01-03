class Student:
    schollname="luminatechnob" #static variable
    def setval(self,id,name):
        self.id=id
        self.name=name
    def printval(self):
        print(self.id,"==",self.name,"==",Student.schollname)

    @classmethod
    def setschool(cls,name): #class method
        cls.schollname=name #change the static variable

    @staticmethod
    def greetings(): #static method
        print("welcome")

s=Student()
s.setval(100,"noname")
s.printval()
s.setschool("lumina Technolb sol")
s.printval()
Student.greetings()#invoking static method by using class name
