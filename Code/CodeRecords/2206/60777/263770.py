t=int(input())

def fun(x):
    res=0
    count=1
    for i in range(1,x+1):
        temp=1
        for j in range(count,count+i):
            temp*=j
            count+=1
        res+=temp
    return res

for i in range(t):
    print(fun(int(input())))
    