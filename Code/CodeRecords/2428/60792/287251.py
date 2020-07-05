num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    list2=[]
    list3=[]
    for j in range(0,n):
        if list1[j]%2==0:
            list2.append(list1[j])
        else:
            list3.append(list1[j])
    list2.sort()
    list3.sort()
    list3=list3[::-1]
    list3=list3+list2
    for k in range(0,len(list3)):
        print(list3[k],end=" ")
    print()    