n=int(input())
arr=list(map(int,input().split()))
arr.sort()
x1=arr[-3]
x2=arr[-2]
x3=arr[-1]

if x1+x2>x3 and x2+x3>x1 and x1+x3>x2 and x1-x2<x3 and x1-x3<x2 and x2-x1<x3 and x2-x3<x1 and x3-x1<x2 and x3-x2<x1:
    print("YES")
else:
    print("NO")