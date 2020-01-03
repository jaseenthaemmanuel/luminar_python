no1=int(input("enter the value no1"))
no2=int(input("enter the value 2"))
lst=[10,20,30]
try:
    res=no1/no2
    print("result=",res)
except Exception as e:
    print(e.args)

try:
    print(lst[5])
except Exception as e:
    print(e.args)
finally:
    print("I have one database connection")