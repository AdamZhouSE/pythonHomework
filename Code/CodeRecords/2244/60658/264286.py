def reve(x):
    ans = 0
    while x:
        ans = ans*10+x%10
        x//=10
    return ans
def isprime(x):
    return x>1 and all(x%i for i in range(2,int(x**0.5)+1))

n = int(input())
while True:
    if isprime(n) and reve(n)==n:
        print(n)
        exit()
    n+=1
    if 10**7<n<10**8:
        n = 10**8