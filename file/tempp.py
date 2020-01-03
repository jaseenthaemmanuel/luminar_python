f=open('/home/jaseentha/PycharmProjects/newproject/file/temp','r')
dict={}
for temp in f:
    temp=temp.rstrip()
    data=temp.split(" ")
    district=data[0]
    tem=data[1]
    print("temparature:",tem)
    print("district:",district)
    print("\n")
    if district not in dict:
        dict[district]=tem
    else:
        old=dict[district]
        if(old<tem):
            dict[district]=tem
        else:
            dict[district]=old
for i in dict:
    print(dict)
    break;


