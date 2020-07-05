def isPrime(num):
    if(num<=2):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

def count(l,r):
    cnt = 0
    for i in range(l,r+1):
        temp = bin(i).count("1")
        if(isPrime(temp)):
            cnt += 1
    return cnt

numOfTests = int(input())
for i in range(numOfTests):
    temp = input().split()
    print(count(int(temp[0]),int(temp[1])))