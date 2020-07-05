def twoSum(numbers, target):
    result = []

    length = len(numbers)

    for i in range(length - 1):
        for j in range(i + 1, length):
            sum1 = numbers[i] + numbers[j]
            if sum1 == target:
                result.append(i + 1)
                result.append(j + 1)
                return result
            elif sum1 < target:
                continue
            elif sum1 > target:
                break
    if(len(result)==0):return None
    else:return result

rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
target=int(input())
print(twoSum(nums,target))