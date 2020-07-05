n=int(input())
ss=input().split(' ')
a=[0 for i in range(10)]
index=0
MIN=0x7f7f7f7f
j=0
for i in range(1,10):
    a[i]=int(ss[j])
    j+=1
    if a[i]<=MIN:
        MIN=a[i]
        index=i
if n<MIN:
    print(-1)
else:
    mod=n%MIN
    for i in range(int(n/MIN)):
        for j in range(9,index-1,-1):
            if (mod+a[index]-a[j])>=0:
                print(j,end='')
                mod-=a[j]-a[index]
                break
    print()