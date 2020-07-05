tests = input()
nums = []
arrays = []
for i in range(int(tests)):
    nums.append(input())
    arrays.append(input())
for i in range(int(tests)):
    num = nums[i].split(' ')
    array = arrays[i].split(' ')
    for j in range(len(array)):
        array[j] = int(array[j])
    maxSub = 0
    subArray = []
    for k in range(int(num[1])-1):
        subArray.append(0)
    for n in range(int(num[0])):
        subArray.append(array.pop(0))
        if maxSub <= sum(subArray):
            maxSub = sum(subArray)
        subArray.pop(0)
    print(maxSub)

# 程序结束
