def getaround(l, i, j):
    result = [[]for n in range(4)]

    if 0 < i < len(l)-1 and 0 < j < len(l)-1:
        result[0].append(i-1)
        result[0].append(j) #上
        result[1].append(i + 1)
        result[1].append(j) #下
        result[2].append(i)
        result[2].append(j-1) #左
        result[3].append(i)
        result[3].append(j+1) #右
    elif i == 0 and j == 0:
        result[0].append(i)
        result[0].append(j + 1)
        result[1].append(i + 1)
        result[1].append(j)
    elif i == 0 and j == len(l)-1:
        result[0].append(i)
        result[0].append(j-1)
        result[1].append(i + 1)
        result[1].append(j)
    elif i == len(l)-1 and j == 0:
        result[0].append(i - 1)
        result[0].append(j)
        result[1].append(i)
        result[1].append(j+1)
    elif i == len(l)-1 and j == len(l)-1:
        result[0].append(i - 1)
        result[0].append(j)
        result[1].append(i)
        result[1].append(j - 1)
    elif i == 0 and 1 < j < len(l)-1:
        result[0].append(i+1)
        result[0].append(j)
        result[1].append(i)
        result[1].append(j-1)
        result[2].append(i)
        result[2].append(j+1)
    elif i == len(l)-1 and 1 < j < len(l)-1:
        result[0].append(i - 1)
        result[0].append(j)
        result[1].append(i)
        result[1].append(j - 1)
        result[2].append(i)
        result[2].append(j + 1)
    elif j == 0 and 1 < i < len(l)-1:
        result[0].append(i - 1)
        result[0].append(j)
        result[1].append(i + 1)
        result[1].append(j)
        result[2].append(i)
        result[2].append(j + 1)
    elif j == len(l)-1 and 1 < i < len(l)-1:
        result[0].append(i - 1)
        result[0].append(j)
        result[1].append(i + 1)
        result[1].append(j)
        result[2].append(i)
        result[2].append(j - 1)

    storage = []
    for m in range(len(result)):
        if result[m]:
            storage.append(l[result[m][0]][result[m][1]])

    if storage.count('o') % 2 != 0:
        return False
    return True


n = int(input())
string = []
for i in range(n):
    string.append(input())
l = [[]for i in range(n)]
for i in range(n):
    for j in range(len(string[i])):
        if string[i][j].isalpha():
            l[i].append(string[i][j])

boolean = True
for i in range(n):
    for j in range(n):
        if not getaround(l, i, j):
            boolean = False
            break

if boolean:
    print("YES")
else:
    print("NO")
