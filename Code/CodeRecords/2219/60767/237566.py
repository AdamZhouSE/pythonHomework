import math
def isAddition(num):
    n = int(math.sqrt(num))
    left = 1
    right = n
    while(left<=right):
        val = left*left+right*right
        if(val == num):
            return True
        elif(val<num):
            left = left+1
        else:
            right = right-1
    return False
num = int(input())
print(isAddition(num))
