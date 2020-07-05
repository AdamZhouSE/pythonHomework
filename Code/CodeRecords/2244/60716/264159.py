def checkPrime(n):
    for i in range(2,n//2+1):
        if n%i ==0:
            return False
    return True

def checkPalindrome(n):
    strs = str(n)
    for i in range((len(strs)+1)//2):
        if strs[i]!=strs[len(strs)-1-i]:
            return False
    return True

n = int(input())
while True:
    check1 = checkPrime(n)
    check2 = checkPalindrome(n)
    if check1 and check2:
        print(n)
        break
    n+=1