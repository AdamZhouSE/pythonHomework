import math
lists = list(map(int, input().split(",")))
threshold = int(input())

dividend = 1
total = sum(lists)
while total > threshold:
    arr = []
    dividend += 1
    for i in range(lists.__len__()):
        temp = math.ceil(int(lists[i]) / dividend)
        arr.append(temp)
    #print(arr)
    total = sum(arr)
    #print(total)

print(dividend)