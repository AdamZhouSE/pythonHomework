v=int(input())
ss=input()
a=[int(i) for i in ss.split(' ')]
n,cnt,mi=0,0,1e9
for i in a:
    mi=min(mi,i)
if n<mi:
    print(-1)
cnt=n/mi
while cnt>0:
    for i in range(8,-1,-1):
        if n-a[i]/mi == cnt and n-a[i] >=0 :
            print(i+1)
            break
    n=n-a[i]
    cnt-=1