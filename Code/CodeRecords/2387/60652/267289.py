n,m=map(int,input().split())
a=list(map(int,input().split()))
for op in range(m):
    flag,l,r=map(int,input().split())
    if flag==0:
        tmp=a[l-1:r]
        tmp.sort(reverse=False)
        a=a[:l-1]+tmp+a[r:]
    if flag==1:
        tmp=a[l-1:r]
        tmp.sort(reverse=True)
        a=a[:l-1]+tmp+a[r:]
q=int(input())-1
print(a[q])