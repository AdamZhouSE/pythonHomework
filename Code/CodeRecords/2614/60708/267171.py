N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    list1=[]
    for item in temp:
        list1.append(int(item))
    temp=input().split(" ")
    list2=[]
    for item in temp:
        list2.append(int(item))
    temp=input().split(" ")
    list3=[]
    for item in temp:
        list3.append(int(item))
    result=0
    for i in range(0,l):
        a=list1[i]-list2[i]
        for item in list3:
            if a==item:
                result=result+1
    print(result)
