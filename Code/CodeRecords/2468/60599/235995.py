n=int(input())
for i in range(n):
    k=int(input())
    s=list(map(int,input().split(' ')))
    res=[]
    count = 1
    op=""
    for z in s:
        count*=z
    for z in s:
        res.append(count//z)
    for z in res:
        op+=str(z)+" "
    print(op[:len(op)])