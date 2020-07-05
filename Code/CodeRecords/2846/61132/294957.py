n=int(input())
l=list(map(int,input().split()))
print(len(list(set(l)))-l.count(0))
