def find(n):
    if n==1:return 3
    if n==2:return 8
    #na
    this=1
    #(n-1)a,1b/1c
    this+=2*n
    #(n-3)a,2c,1b
    this+=int(n*(n-1)*(n-2)/2)
    #(n-2)a,2c
    this+=int(n*(n-1)/2)
    #(n-2)a,1b,1c
    this+=n*(n-1)
    return this

t=int(input())
res = []
for i in range(t):
    n=int(input())
    res.append(find(n))
for e in res:print(e)