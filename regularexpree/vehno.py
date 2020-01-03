import re
str=input("enter the number")
x='KL\s\d{2}\s[A-Z]{2}\s\d{4}'
matcher=re.fullmatch(x,str)
if(matcher!=None):
    print("valid")
else:
    print("invalid")
