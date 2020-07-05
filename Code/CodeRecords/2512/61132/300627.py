t,k = map(int,input().split())
l=list(map(int,input().split()))
t=int(input())
ans=[]
for j in range(t):
    tmp=list(map(int,input().split()))
    if tmp[0]==1:
        l[tmp[1]:tmp[2]+1]=map(lambda x:l[3]*x,l[tmp[1]:tmp[2]+1])
    elif tmp[0]==2:
        l[tmp[1]:tmp[2]+1] = map(lambda x: l[3]+x, l[tmp[1]:tmp[2] + 1])
    else:
        print(sum([i for i in l if tmp[1]<=i<=tmp[2]])%k)