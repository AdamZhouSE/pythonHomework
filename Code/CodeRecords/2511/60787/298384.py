n,s=map(int,input().split())
a=[]
for i in range(0,n):
    a.append(int(input()))
for j in range(0,n-1):
    re=0
    for i in range(j,j+(n-j)//2):
        if sum(a[0:i])<=s and sum(a[i:2*i])<=s:
            re=2*(i-j)
    print(re)
print(0)