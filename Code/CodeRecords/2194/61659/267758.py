def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

T=int(input())

for i in range(0,T):
    temp=list(input().split(" "))
    start=int(temp[0])
    end=int(temp[1])

    store=[]
    for i in range(start,end+1):
        if isPrime(i):
            store.append(str(i))

    print(' '.join(store))