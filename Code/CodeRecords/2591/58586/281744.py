nums=int(input())
def isPrime(temp):
    for i in range(2,int(pow(temp,0.5))):
        if temp%i==0:
            return False
    return True
for i in range(nums):
    temp=int(input())
    if isPrime(temp+2):
        print("Yes")
    else:
        print("No")