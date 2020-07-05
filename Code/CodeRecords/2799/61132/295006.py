def ori(n):
    while n%2==0:
        n=n//2
    while n%3==0:
        n=n/3
    return n

n=int(input())
l=list(map(int,input().split()))
tmp=ori(l.pop())
for i in l:
    if ori(i)!=tmp:
        print("No")
        break
else:
    print("Yes")