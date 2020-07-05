n=int(input())
l=list(map(int,input().split()))
tmp=len(l)-l.count(0)
print(len(list(set(l)))+(-1 if l.count(0) else 0))
