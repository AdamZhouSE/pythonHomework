def count(x,i,j):
    cc=x[i]
    for k in range(i,j+1):
        if x[k]<cc:
            cc=x[k]
    return (j-i+1)*cc
n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=0
    for q in range(0,len(b)-1):
        for w in range(q+1,len(b)):
            if count(b,q,w)>c:
                c=count(b,q,w)
    print(c)
    