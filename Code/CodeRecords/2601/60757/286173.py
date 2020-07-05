m=int(input())
n=int(input())
k=int(input())
li=[]
for i in range(1,m+1):
    for j in range(1,n+1):
        li.append(i*j)
li=sorted(li)
print(li[k-1])