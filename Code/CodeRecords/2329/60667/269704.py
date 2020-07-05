A = list(map(int, input().split(',')))
temp = []
for i in A:
    temp.append([i])
for i in range(len(A)):
    for j in A[i+1:]:
        for x in range(2, A[i]+1):
            if A[i] % x == 0 and j % x == 0:
                temp[i].append(j)
                break
for i in range(len(A)):
    for j in temp[:i]+temp[i+1:]:
        if A[i] in j:
            temp[i] = temp[i] + j
newtemp = []
for i in temp:
    newtemp.append([])
for i in range(len(A)):
    for j in temp[i]:
        if j not in newtemp[i]:
            newtemp[i].append(j)
for i in newtemp:
    i.sort()
result = []
for i in range(len(newtemp)):
    check = True
    for j in newtemp[:i]+newtemp[i+1:]:
        if set(newtemp[i]).issubset(j):
            check = False
            if newtemp[i] == j:
                if newtemp[i] not in result:
                    result.append(newtemp[i])
    if check:
        result.append(newtemp[i])

maximum = 0
for i in result:
    if len(i) > maximum:
        maximum = len(i)
print(maximum)