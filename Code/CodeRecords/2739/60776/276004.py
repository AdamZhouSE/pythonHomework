def chazhao(list1,listm,list3,a,zongshu):
    if(len(list1)<a):
        listm.clear()
    if a==1:
        if zongshu in list1:
            listm.append(zongshu)
            list3.append(listm)
    else:
        for i in range(0,len(list1)):
            listx=[]
            listx.extend(listm)
            listx.append(list1[i])
            chazhao(list1[i+1:len(list1)],listx,list3,a-1,zongshu-list1[i])


if __name__ == "__main__":
    list1=[1,2,3,4,5,6,7,8,9]
    list2=[]
    list3=[[]]
    a=input()
    k=int(a[0])
    n=int(a[3])
    chazhao(list1,list2,list3,k,n)
    del list3[0]
    print(list3)