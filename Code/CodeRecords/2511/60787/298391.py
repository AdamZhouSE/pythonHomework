n,s=map(int,input().split())
a=[]
for i in range(0,n):
    a.append(int(input()))
for j in range(0,n-1):
    re=0
    for i in range(0,(n-j)//2+1):
        if sum(a[j:j+i])<=s and sum(a[j+i:j+2*i])<=s:
            re=2*i
    print(re)
print(0)