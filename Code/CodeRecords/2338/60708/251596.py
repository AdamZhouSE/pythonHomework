Q=int(input())#问题数
result=["No"]*Q
for i in range(0,Q):
    temp=input()
    l=int(temp.split(" ")[0])
    X=int(temp.split(" ")[1])
    listtemp=input().split(" ")
    list1=[]
    list2=[]
    for item in listtemp:
        list1.append(int(item))
        list2.append(int(item))
    for x in range(0,l):
        list1[x]=X-list1[x]
    for item in list1:
        if item in list2:
            result[i]="Yes"
for item in result:
    print(item)