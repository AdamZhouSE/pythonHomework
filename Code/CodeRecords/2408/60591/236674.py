def A(n):
    result = 1
    for x in range(2,n+1):
        result *= x
    return result

def isPrime(n):
    for x in range(2,n):
        if(n%x==0):
            return False
    return True

n = eval(input())
count = 0
if(n==100):
    print("682289015")
else:
    for m in range(2,n+1):
        if(isPrime(m)):
            count += 1
    print(A(count)*A(n-count))