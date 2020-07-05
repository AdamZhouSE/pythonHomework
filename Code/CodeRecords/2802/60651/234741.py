list1=input().split()
list1=[int(x) for x in list1]
n=list1[0]
m=list1[1]
list2=input().split()
list2=[int(x) for x in list2]
for  j in range(n):
    while(list2[j]>m):
        for i in range(n):
            list2[i]-=m
for p in range(n-1,-1,-1):
    if list2[p]>0:
        print(p+1)
        break
        
