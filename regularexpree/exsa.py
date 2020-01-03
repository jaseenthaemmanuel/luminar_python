import re
x='[a-kA-K][369][a-zA-k]*'
str=input("enter the string")
matcher=re.fullmatch(x,str)
if(matcher!=None):
    print("valid")
else:
    print("invalid")