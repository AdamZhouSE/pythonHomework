num=int(input())
for nn in range(num):
    n=int(input())
    li=[0 for i in range(n+1)]
    li[0]=1
    for i in range(3,n+1):
        li[i]+=li[i-3]
    for i in range(5,n+1):
        li[i]+=li[i-5]
    for i in range(10,n+1):
        li[i]+=li[i-10]
    print(li[n])