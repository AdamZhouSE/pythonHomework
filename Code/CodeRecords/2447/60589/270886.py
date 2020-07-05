mn=input().split(' ')
m=int(mn[0])
n=int(mn[1])
l=list(map(int,input().split(' ')))
ans=[]
for i in range(n):
    ab=input().split(' ')
    a=int(ab[0])
    b=int(ab[1])
    sub_l=l[a-1:b]
    mi=min(sub_l)
    ans.append(mi)
ans=list(map(str,ans))
print(' '.join(ans)+' ',end='')