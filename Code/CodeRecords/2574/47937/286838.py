from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n=int(input())

#print(n)

i=0
while i<n:
    b=int(input())
    #
    zhishu=2
    start=1
    while start<b:
        if(is_prime(zhishu)==True):
            start=start+1
        zhishu+=1
    zhishu-=1
    print(zhishu*zhishu+1)
    i=i+1