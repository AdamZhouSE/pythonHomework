#22
def isPrime (num):
    isOK = True
    for i in range(2,int(num)):
        if int(num) % i == 0:
            isOK = False
            break
    return isOK
def isPalindrome (num):
    isOK = True
    n = len(num)
    for i in range(0,n//2):
        if num[i] != num[n-1-i]:
            isOK = False
            break
    return isOK
N = int(input())
i = 2
while True:
    if i >= N and isPrime(str(i))==True and isPalindrome(str(i))==True:
        break
    else:
        i += 1
print(i)
