n=int(input())
a=[int(n) for n in input().split()]
list1=[]
for i in range(0,n):
    if a[i]==1:
        list1.append(i)
re=0
for j in range(0,len(list1)-1):
    re=re+list1[j+1]-list1[j]
print(re)