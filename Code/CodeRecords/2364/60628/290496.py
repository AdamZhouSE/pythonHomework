def isNumWithDupDigits(n):
    s = sorted(str(n))
    if len(s) == 1:
        return 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return 1
    if s[-1] == s[-2]:
        return 1
    return 0

def numOfNumWithDupDigits(N):
    count = 0
    for n in range(N+1):
        if isNumWithDupDigits(n):
            count += 1
    return count

N = int(input())
print(numOfNumWithDupDigits(N))