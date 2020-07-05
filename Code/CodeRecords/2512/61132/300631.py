t,k = map(int,input().split())
l=list(map(int,input().split()))
t=int(input())
for j in range(t):
    tmp=list(map(int,input().split()))
    if tmp[0]==1:
        l[tmp[1]-1:tmp[2]]=map(lambda x:tmp[3]*x,l[tmp[1]-1:tmp[2]])
    elif tmp[0]==2:
        l[tmp[1]-1:tmp[2]] = map(lambda x: tmp[3]+x, l[tmp[1]-1:tmp[2]])
    else:
        print(sum([l[i] for i in range(len(l)) if tmp[1]-1<=i<=tmp[2]-1])%k)