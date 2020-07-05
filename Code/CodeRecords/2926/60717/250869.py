n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list2=list(set(list1))
maxx=0
for i in list2:
    count=0
    for j in list1:
        if i==j:
            count+=1
    maxx=max(maxx,count)
print(maxx)        