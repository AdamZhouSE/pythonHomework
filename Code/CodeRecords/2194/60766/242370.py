def isPrime(n):
    if n==1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def printPrime(ev):
    res=''
    for i in range(ev[0], ev[1]+1):
        if isPrime(i):
            res=res+' '+str(i)
    print(res[1:])

n=int(input())
num=[]

for i in range(n):
    line=input().split()
    ev=[]
    ev.append(int(line[0]))
    ev.append(int(line[1]))
    num.append(ev)

for i in range(n):
    printPrime(num[i])