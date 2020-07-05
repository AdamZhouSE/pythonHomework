"""
坐标只能直线变动
用一个数组记录已有的坐标，对于每一个点，只要与数组内的坐标横纵坐标有一个相等，就不用新建雪堆
"""
n = int(input())
data = []
for i in range(n):
    data.append([int(x) for x in input().split(" ")])
count = 0
data.sort()
data_x = [data[0][0]]
data_y = [data[0][1]]
for i in range(1, n):
    isEqual = False
    for j in range(len(data_x)):
        if data[i][0] == data_x[j] or data[i][1] == data_y[j]:
            isEqual = True
            break
    if not isEqual:
        count += 1
    data_x.append(data[i][0])
    data_y.append(data[i][1])
print(count)
