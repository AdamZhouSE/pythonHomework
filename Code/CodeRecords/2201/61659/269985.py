T=int(input())

def isPrime(x):
    if x==1 or x==0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True


for i in range(0,T):
    temp=list(input().split(" "))
    start=int(temp[0])+int(temp[1])

    j=1
    while True:
        if isPrime(start+j):
            print(j)
            break
        j=j+1