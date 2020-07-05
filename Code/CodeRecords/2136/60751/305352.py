import math

def id(n,m):
    k=2
    is_=False
    while(True):
        if n == (math.pow(k, m) - 1) // (k - 1):
            is_=True
            break
        if n<(math.pow(k, m) - 1) // (k - 1):
            break
        k+=1
    return is_,k
num=int(input())

k=int(math.log(num+1,2))+1

jinzhi=0
for i in range(k):
    weishu,jinzhi=id(num,k-i)
    if weishu:break
print(jinzhi)
