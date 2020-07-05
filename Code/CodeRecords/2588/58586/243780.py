nums=int(input())
def partition(num):
    sum=0
    while num>0:
        sum+=num%10
        num=num//10
    return sum
def isPrime(num):
    for i in range(2,int(pow(num,0.5))+1):
        if num%i==0:
            return False
    return True
for i in range(nums):
    num=int(input())
    if num==0 or isPrime(num):
        print(0)
    else:
        a = partition(num)
        b = 0
        while num > 1:
            for i in range(2, num + 1):
                if isPrime(i):
                    if num % i == 0:
                        num = num // i
                        b += partition(i)
                        break
        if a == b:
            print(1)
        else:
            print(0)