def isPrime(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return False
    return True

a=int(input())
list=[]
for i in range(1,a):
    if isPrime(i):
        list.append(i)
print(len(list))