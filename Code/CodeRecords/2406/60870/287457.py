nums = int(input())
array = []
for i in range(nums):
    array.append(int(input()))
res = []
for i in range(nums):
    res.append(array[nums - i - 1])
res.sort()
count = -1
for j in range(len(array)):
    for i in range(len(array)):
        goal = res[i]
        if array.index(goal) != i:
            index = array.index(goal)
            temp = array[index]
            array[index] = array[i]
            array[i] = temp
            count = count + 1
print(count)
