n=int(input())
l1=list(map(int,input().split()))
l2=sorted(list(map(int,input().split())))
volume=l2[-1]+l2[-2]
print("YES" if sum(l1)<=volume else "NO")