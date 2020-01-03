import re
no=input("enter the mobile number")
x='^[6-9]\d{9}'
matcher=re.fullmatch(x,no)
if(matcher!=None):
    print("valid")
else:
    print("inalid")