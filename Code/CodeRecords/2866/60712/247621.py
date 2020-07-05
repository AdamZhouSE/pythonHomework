n = int(input())
list1 = list(map(int, input().split()))
nums = []
numOfZero = 0
result = 1
for i in range(n):
    if list1[i] == 1:
        nums.append(numOfZero)
        numOfZero = 0
    else:
        numOfZero +=1
    if i == n - 1:
        nums.append(numOfZero)
        break
for i in range(len(nums)):
    result = result * (nums[i] + 1)
if list1[0]==0:
    result = int(result/(nums[0]+1))
if list1[n-1]==0:
    result = int(result/(nums[len(nums)-1]+1))
print(result)
