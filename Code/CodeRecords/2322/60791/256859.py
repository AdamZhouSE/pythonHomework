import math
def ispalindrome(num):
    temp = str(num)
    if(temp == temp[::-1]):
        return True
    else:
        return False
l = int(input())
r = int(input())
count = 0
for i in range(math.ceil(math.sqrt(l)),int(math.sqrt(r))):
    if(ispalindrome(i)):
        if(ispalindrome(i**2)):
            count += 1
print(count)