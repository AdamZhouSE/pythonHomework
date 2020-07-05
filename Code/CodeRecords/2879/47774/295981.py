n=int(input())
h=[0 for i in range(n*2)]
v=[0 for i in range(n*2)]
a=[0 for i in range(n*2)]
flag=0
for i in range(n*n):
    x,y=map(int,input().split(' '))
    if h[x]==0 and v[y]==0:
        a[flag]=i
        flag+=1
        h[x]=1
        v[y]=1
for i in range(flag):
    if i!=flag-1:
        print(a[i]+1,end=' ')
    else:
        print(a[i]+1,end='')
print()
    