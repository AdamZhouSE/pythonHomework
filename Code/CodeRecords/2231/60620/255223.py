t=int(input())
def su(n):
    if(n==2):
        return 1
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
def s(n):
    num=0
    for i in range(2,n):
        if(n%i==0 and su(i)):
            n=n//i
            for j in range(i+1,n):
                if(n%j==0 and su(j)):
                    n=n//j
                    if(su(n) and j!=n and i!=n):
                        return 1

    return 0
for i in range(t):
    n=int(input())
    print(s(n))