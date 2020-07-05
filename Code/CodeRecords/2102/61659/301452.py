def isPrime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

num=int(input())
res=[]
for i in range(1,num):
    if isPrime(i):
        res.append(i)

print(len(res))

