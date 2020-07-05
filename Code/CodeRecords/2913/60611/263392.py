num=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s%2==0:
    print("YES")
else:
    print("NO")