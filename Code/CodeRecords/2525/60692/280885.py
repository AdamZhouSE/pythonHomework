list1 = []
start = input()[1:-1].split(',')
end = input()[1:-1].split(',')
profit = input()[1:-1].split(',')
for i in range(len(start)):
    list1.append([int(start[i]), int(end[i]), int(profit[i])])
list1.sort()
mark = 0
m = 0
res = 0
list2 = [0 for i in range(len(list1))]
for i in range(len(list1)):
    for j in range(mark, i):
        if list1[i][0] >= list1[j][1]:
            if j == mark:
                mark += 1
            m = max(m, list2[j])
    list2[i] += m + list1[i][2]
    res = max(res, list2[i])
print(res)