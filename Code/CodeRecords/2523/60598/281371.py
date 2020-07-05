s = input()[1:-1]
i = 0
result = []
while i < len(s):
    if s[i] == "[":
        temp = ""
        i += 1
        while s[i] != "]":
            temp += s[i]
            i += 1
        result.append(list(map(int, temp.split(","))))
        i += 1
    else:
        i += 1
row = len(result)
col = len(result[0])
for i in range(row):
    m = i
    n = 0
    temp = []
    while m < row and n < col:
        temp.append(result[m][n])
        m += 1
        n += 1
    temp = sorted(temp)
    m = i
    n = 0
    for k in range(len(temp)):
        result[m][n] = temp[k]
        m += 1
        n += 1
for j in range(col):
    m = 0
    n = j
    temp = []
    while m < row and n < col:
        temp.append(result[m][n])
        m += 1
        n += 1
    temp = sorted(temp)
    m = 0
    n = j
    for k in range(len(temp)):
        result[m][n] = temp[k]
        m += 1
        n += 1
print(result)
