p,n=map(int,input().split())
flag=True
hash=[]
num=0;
for i in range(0,p):
    hash.append(-1)
for i in range(0,n):
    x=int(input())
    num=num+1
    hx=x%p
    if hash[hx]==-1:
        hash[hx]=x
    else:
        print(num)
        flag=False
        break
if flag:
    print(-1)