from math import sqrt
def numOfSuperPalindrome(L, R):
    count = 0
    for i in range(L, R+1):
        if isSuperPalindrome(i):
            j = int(sqrt(i))
            if j * j == i and isSuperPalindrome(j):
                count += 1
    return count

def isSuperPalindrome(n):
    n = str(n)
    length = len(n)
    for i in range(length):
        if n[i] != n[length - i - 1]:
            return 0
    return 1

L = int(input())
R = int(input())
print(numOfSuperPalindrome(L, R))