n=int(input())
for l in range(n):
    res=""
    nu=int(input())
    a=[int(x) for x in input().split(" ")]
    for i in range(1,nu+1):
        if not i in a:
            res=res+str(i)
            break
    for i in range(0,nu-1):
        judge=0
        for j in range(i+1,nu):
            if a[i]==a[j]:
                res=str(a[i])+" "+res
                judge=1
            break
        if judge==1:
            break
    if res=="":
        res="0 0"
    print(res)