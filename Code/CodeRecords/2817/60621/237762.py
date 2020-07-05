a=int(input())
b=[int(t)-1 for t in input().split()]
for i in range(a):
    num=1
    B=b[i]
    C=b[B]
    if(b[C]==i):
        print("YES")
        break
    if(i==a-1):
        print("NO")