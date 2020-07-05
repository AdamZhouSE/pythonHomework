"""
题目描述
    给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
    如果数组元素个数小于 2，则返回 0。
"""
"""
输入描述
    一个无序的数组
"""
"""
输出描述
    如果元素大于等于2，则输出排序之后，相邻元素之间最大的差值；否则输出0
"""

currInput = input()
sample = currInput[1:-1].split(',')
inputArray = []
for i in sample:
    inputArray = inputArray + [int(i)]
if len(inputArray) < 2:
    print(0)
else:
    for i in range(len(inputArray)):
        for j in range(1,len(inputArray) - i):
            if inputArray[j] < inputArray[j - 1]:
                temp = inputArray[j]
                inputArray[j] = inputArray[j - 1]
                inputArray[j - 1] = temp
    outcome = []
    for i in range(1,len(inputArray)):
        outcome = outcome + [inputArray[i] - inputArray[i - 1]]
    answer = outcome[0]
    for numbers in outcome:
        if numbers > answer:
            answer = numbers
    print(answer)