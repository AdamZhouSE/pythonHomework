m=int(input())
n=int(input())
res=[]
if m==0 and n==0:
    print([0,0])
else:
    for i in range(n):
        if 4*i+2*(n-i)==m:
            res.append(i)
            res.append(n-i)
            break
    print(res)