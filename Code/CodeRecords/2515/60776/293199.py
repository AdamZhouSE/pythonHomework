a=10000
def digui(list1,list2,huafen):
    if huafen==1:
        max=0
        global a
        list2.append(list1)
        for i in range(0,len(list2)):
            if sum(list2[i])>max:
                max=sum((list2[i]))
        if max<a:
            a=max
    else:
        for i in range(1,len(list1)-huafen+1):
            list3=[]
            list3.extend(list2)
            list3.append(list1[0:i])
            digui(list1[i:len(list1)],list3,huafen-1)





if __name__ == "__main__":
    b=input().split(',')
    for i in range(0,len(b)):
        b[i]=int(b[i])
    list=[]
    c=int(input())
    digui(b,list,c)
    print(a)