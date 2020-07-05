def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


n=int(input())
while True:
    s=str(n)
    r=s[::-1]
    if s==r and is_prime(n):
        print(n)
        break
    n+=1