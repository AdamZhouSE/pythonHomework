m=int(input())
n=int(input())
k=int(input())
list=[]
for i in range(1,m+1):
    for j in range(1,n+1):
        list.append(i*j)
list.sort()
print(list[k-1])