n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list2=[]
maxx=0
for i in range(0,n):
    if list1[i] in list2:
        list2.remove(list1[i])
    else:
        list2.append(list1[i])
    maxx=max(maxx,len(list2))
print(maxx)    