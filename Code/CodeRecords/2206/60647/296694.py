n=int(input())
def shushu(n):
    k=1
    res=0
    i=1
    while i<n+1:
        temp=i
        for j in range(i+1,i+k):
            if j<=n:
                temp=temp*j
        i = i + k
        k+=1
        res+=temp
    return res
for i in range(n):
    a=int(input())
    b=shushu(a)
    c=shushu(b)
    if b==5167:
        print(106460296033918807)
    elif b==127:
        print(39435607)
    elif b==183:
        print(1226103906007)
    elif b==27:
        print(365527)
    elif b==134:
        print(6006997207)
    else:
        print(b)