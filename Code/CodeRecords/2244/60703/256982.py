def isPrime(p):
    for i in range(2,p):
        if(p%i==0):
            return False
    return True

def isPalindrome(q):
    if(
        q == int("".join(reversed(str(q))))
    ):
        return True
    else:
        return False

n = int(input())
while True:
    if(
        isPalindrome(n)
    ):
        if(
            isPrime(n)
        ):
            print(n)
            break
    n+=1