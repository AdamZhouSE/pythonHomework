n=int(input())
a=list(map(int,input().split(" ")))
s=0
d=0
for i in range(0,n):
    Max=max(a[0],a[len(a)-1])
    if i%2==0:
        s+=Max
    else:
        d+=Max
    a.remove(Max)         
print(f'{s} {d}')          