n=int(input())
m=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
a.sort()
m0=0
count=0
for i in range(0,n):
    m0+=a[n-i-1]
    count+=1
    if(m0>=m):
        break
print(count)