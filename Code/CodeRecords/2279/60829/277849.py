def sum(x):
    res=0
    for i in x:
        res=res+i
    return res
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")][1]
    b=[int(x) for x in input().split(" ")]
    judge=0
    for j in range(0,len(b)-1):
        for k in range(j+1,len(b)):
            if sum(b[j:k+1])==a:
                print(str(j+1)+" "+str(k+1))
                judge=1
                break
        if judge==1:
            break
    if judge==0:
        print("-1")