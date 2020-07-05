import math

def isplalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

lower = int(input())
upper = int(input())
l = []
for i in range(lower, upper+1):
    if int(math.sqrt(i)) * int(math.sqrt(i)) == i:
         if isplalindrome(i) and isplalindrome(int(math.sqrt(i))):
            l.append(i)
print(len(l))