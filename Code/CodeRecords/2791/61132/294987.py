n=int(input())
l=list(map(int,input().split()))
print(l.count(1))
print(' '.join([str(l[i]) for i in range(len(l)) if i==len(l)-1 or l[i+1]<=l[i]]))