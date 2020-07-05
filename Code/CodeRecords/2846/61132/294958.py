n=int(input())
l=list(set(list(map(int,input().split()))))
print(len(l)-l.count(0))
