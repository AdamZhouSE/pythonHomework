import math
def isPrime(n):
    if n==2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def isSmith(num,string):
    summ = Sep(string)
    count=0
    for i in range(2,num):
        if isPrime(i) and num%i==0:
            if i>9:
                count += Sep(i)
            else:
                count+=i
            num=num//i
            i=2               
        if num == 1 :
            break
    if count == summ:
        return 1
    else:
        return 0
def    Sep(num):
    num = str(num)
    res=0
    for i in range(0,len(num)):
        res+=int(num[i])
    return res
    
n = int(input())
for i in range(0,n):
    a=input()
    print(isSmith(int(a),a))