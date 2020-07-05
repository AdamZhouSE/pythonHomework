l1=input().split()
n=int(l1[0])
s=int(l1[1])
a=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
for j in range(0,n):
    max1=0
    for k in range(1,(n-j)//2+1):
        if(sum(a[j:j+k])<=s and sum(a[j+k:j+2*k])<=s):
            max1=2*k
    print(max1)