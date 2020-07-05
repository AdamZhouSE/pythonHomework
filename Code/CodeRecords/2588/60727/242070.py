def isPrime(num):
    if num == 2:
        return True
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True
def isSmith(num):
    count=0
    while num!=1:
        for i in range(2,num):
            if isPrime(i) and num%i==0:
                count += i
                num=num//i
                break
    if count == num:
        return 1
    else:
        return 0
n = int(input())
for i in range(0,n):
    a=int(input())
    print(isSmith(a))
                