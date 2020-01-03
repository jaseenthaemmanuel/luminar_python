class Student:
    def setDetails(self,name,rollno,depa):
        self.name=name
        self.rollno=rollno
        self.department=depa
    def display(self):
        print("student name:",self.name)
        print("roll no:",self.rollno)
        print("department:",self.department)
    def __str__(self):
        return self.name
list=[]
s=Student()
s.setDetails("akhi",45,"cs")
s.display()
print("\n")
s1=Student()
s1.setDetails("aki",48,"it")
s1.display()
print(s)
list.append(s)
list.append(s1)
for s in list:
    print(s)
