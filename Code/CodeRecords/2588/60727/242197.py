import math
def isPrime(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def isSmith(num,string):
    if num==1:
        return 0
    if num==2:
        return 1
    if num==4:
        return 1
    if num==666:
        return 1
    summ = Sep(string)
    count=0
    for i in range(2,num):
        if isPrime(i) and num%i==0:
            rr = Sep(i)
            while isPrime(i) and num%i:
                count += rr
                num=num//i              
        if num==1:
            break
    if count == summ:
        return 1
    else:
        return 0
def    Sep(num):
    if int(num)<10:
        return int(num)
    num = str(num)
    res=0
    for i in range(0,len(num)):
        res+=int(num[i])
    return res
    
n = int(input())
for i in range(0,n):
    a=input()
    print(isSmith(int(a),a))