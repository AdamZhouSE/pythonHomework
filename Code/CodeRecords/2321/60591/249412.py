def generate(basic,n,N,result):
    if(n == 0):
        if(eval(result) <= N):
            return 1
        else:
            return 0
    else:
        n = n - 1
        res = 0
        for x in basic:
            temp = result + x
            res += generate(basic,n,N,temp)
        return res

D = input().split(",")
N = input()
length = len(N)
N = eval(N)
res = 0
for x in range(1,length+1):
    res += generate(D,x,N,"")
print(res)