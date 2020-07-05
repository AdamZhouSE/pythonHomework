info=input().split()
n=int(info[0])
cases=int(info[1])
src=[i+1 for i in range(n)]
def reverse_in_array(src,l,r):
    tmp=list(reversed(src[l:r]))
    for i in range(l,r):
        src[i]=tmp[i-l]
for c in range(cases):
    info=input().split()
    l=int(info[0])-1
    r=int(info[1])
    reverse_in_array(src,l,r)
print(*src,end=' ')