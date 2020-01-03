import re
str=input("enter the gmail")
x='[a-z]{1}[a-zA-Z0-9]*@gmail.com$'
matcher=re.fullmatch(x,str)
if(matcher!=None):
    print("valid")
else:
    print("invalid")