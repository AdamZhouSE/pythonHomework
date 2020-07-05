l=input().split(',')
l=list(map(int,l))
l.sort()
n=len(l)
has=False
for i in range(1,n-1):
    if l[n-i-2]+l[n-i-1]>l[n-i]:
        print(l[n-i-2]+l[n-i-1]+l[n-i])
        has=True
        break
if not has:
    print(0)