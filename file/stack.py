list=[]
top=0
def push(ele):
    if(top>5):
        print("stack is full")
    else:
        list[top]=ele
        top+=1
def pop():
    if(top<0):
        print("stack is empty")
    else:
        top-=1
def traverse():
    for i in list:
        print(i)
ch=int(input("enter the choice 1.push 2.pop 3.travers"))
print("\n")
if(ch==1):
    ele=int(input("enter the element"))
    push(ele)
elif(ch==2):
    pop()
elif(ch==3):
    traverse()
else:
    print("u entered wrong choice")


