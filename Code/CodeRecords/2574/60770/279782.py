def solve():
    n=int(input())
    res=1
    while(n>0):
        res += 1
        while(not isPrime(res)):
            res+=1
        n-=1
        
    print(1+res**2)

def isPrime(n):
    half=int(n**0.5)
    for i in range(2,half+1):
        if n%i==0:
            return False
    return True

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()