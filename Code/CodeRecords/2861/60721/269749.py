n=int(input())
lis=list(map(int,input().split(' ')))
lis.sort()
re=0
for i in range(1,n,2):
    re=re+lis[i]-lis[i-1]
print(re)