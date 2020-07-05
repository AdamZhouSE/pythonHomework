def isPrime(num):
    if(num==1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

num = int(input())
cnt = 0
for i in range(1,num):
    if(isPrime(i)):
        cnt = cnt + 1
print(cnt)