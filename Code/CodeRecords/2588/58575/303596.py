import math

res=[]
def isPrime(n):
    if n==1:
        return False
    judge=True
    i=2
    while i<int(math.sqrt(n))+1:
        if n%i==0:
            return False
        i+=1
    return True

def suShu(number):
    if number==1:
        return 1
    i=2
    while i<=number:
        if isPrime(i)==False:
            i+=1
            continue
        if number%i==0:
            res.append(i)
            suShu(number//i)
            return
        i+=1

n=int(input())
for i in range(n):
    number=int(input())
    suShu(number)

    if isPrime(number)==True:
        print(0)
    else:
        first=0
        while number!=0:
            first+=number%10
            number=number//10

        second=0
        for i in res:
            while i!=0:
                second+=i%10
                i=i//10
        if first==second:
            print(1)
        else:
            print(0)
    res.clear()