n=int(input())
list1=[]
for i in range(0,n):
    tmp=input().split()
    x=int(tmp[0])
    y=int(tmp[1])
    list1.append([x,y])
list2=[1 for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if list1[i][0]==list1[j][0] or list1[i][1]==list1[j][1]:
            list2[i]=0
print(list2.count(1)-1)            