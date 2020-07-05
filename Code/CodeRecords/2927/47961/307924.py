a=[int(i) for i in input().split()]
n=a[0]
d=a[1]
nums=int(input())
for i in range(0,nums):
    dian=[int(i) for i in input().split()]
    x=dian[0]
    y=dian[1]
    if abs(x-y)<=d and abs(x+y)<=(2*n-d) and abs(x+y)>=d:
        print("YES")
    else:
        print("NO")
        