def x20(s,l,n):
    if not l:return n
    for i in range(len(l)):
        if l[i]>s:
            break
    else:
        return n
    return max(x20(l[i],l[i+1:],n+1),x20(s,l[i+1:],n))

n = int(input())
for j in range(n):
    l=list(input())
    print(x20('',l,0))