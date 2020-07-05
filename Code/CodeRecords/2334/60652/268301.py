def perimeter(a1,a2,a3):
    if a1+a2>a3 and a1+a3>a2 and a2+a3>a1:
        return a1+a2+a3
    return 0


a=list(map(int,input().split(',')))
n=len(a)
MAX=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            MAX=max(MAX,perimeter(a[i],a[j],a[k]))
print(MAX)            