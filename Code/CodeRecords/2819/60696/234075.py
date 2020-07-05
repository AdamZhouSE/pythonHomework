n = int(input())
arr = input()
numsInGroup = [int(i) for i in arr.split()]
result = 0
numOfOne = numsInGroup.count(1)
numOfTwo = numsInGroup.count(2)
numOfThree = numsInGroup.count(3)
numOfFour = n - numOfOne - numOfTwo - numOfThree
if numOfOne <= numOfThree:
    result = int(numOfTwo/2) + numOfTwo%2 + numOfThree + numOfFour
else:
    result = numOfThree + numOfFour + int(numOfTwo/2) + int((numOfOne-numOfThree)/4)
    if (numOfOne-numOfThree)%4 + (numOfTwo%2) * 2 > 4:
        result += 2
    elif (numOfOne-numOfThree)%4 + (numOfTwo%2) * 2 == 0:
        pass
    else:
        result += 1
print(int(result))