def mul(before,num):
    res=1
    for i in range(before,num+before):
        res*=(i+1)
    return res
t = int(input())
for i in range(t):
    n=int(input())
    numsBefore=0
    res=0
    for i in range(n):
        res+=mul(numsBefore,i+1)
        numsBefore=numsBefore+i+1
    print(res)