import operator
f=open('/home/jaseentha/PycharmProjects/newproject/file/fakefriends.csv','r')
dict={}
count=0
for item in f:
    item=item.rstrip()
    data=item.split(",")
    name=data[1]
    age=data[2]
    print("name",name)
    print("age",age)
    if age not in dict:
        dict[age]=1
    else:
        dict[age]+=1

sorted_d=sorted(dict.items(),key=operator.itemgetter(-1))
print(sorted_d)


