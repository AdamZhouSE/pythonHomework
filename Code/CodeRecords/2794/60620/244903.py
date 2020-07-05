n=int(input())
a=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
s=0
number=[]
for i in range(n):
    s+=a[i]
    number.append(s)
for i in range(m):
    for j in range(n-1):
        if(q[i]>number[j] and q[i]<=number[j+1]):
            print(j+2)
    if(q[i]<=number[0]):
        print(1)
    if(q[i]>number[n-1]):
        print(n)