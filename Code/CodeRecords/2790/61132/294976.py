n,m=input().split()
l1=sorted(list(map(int,input().split())))
l2=list(map(int,input().split()))
ans=[str(len([j for j in l1 if j<=i])) for i in l2]
print(' '.join(ans))