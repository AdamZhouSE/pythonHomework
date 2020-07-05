size = int(input())
l = []
signalList = []
for i in range(size):
    l.append(list(input()))
if size == 1:
    print("YES")
else:
    i = 0
    while i < size:
        j = 0
        while j < size:
            result = 0
            if (i == 0 and j == 0):
                if l[i + 1][j] == 'o':
                    result += 1
                if l[i][j + 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif i == size - 1 and j == size - 1:
                if l[i - 1][j] == 'o':
                    result += 1
                if l[i][j - 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif i == size - 1 and j == 0:
                if l[i - 1][j] == 'o':
                    result += 1
                if l[i][j + 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif i == 0 and j == size - 1:
                if l[i + 1][j] == 'o':
                    result += 1
                if l[i][j - 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif i == 0:
                if l[i + 1][j] == 'o':
                    result += 1
                if l[i][j + 1] == 'o':
                    result += 1
                if l[i][j - 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif i == size - 1:
                if l[i - 1][j] == 'o':
                    result += 1
                if l[i][j + 1] == 'o':
                    result += 1
                if l[i][j - 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif j == 0:
                if l[i + 1][j] == 'o':
                    result += 1
                if l[i - 1][j] == 'o':
                    result += 1
                if l[i][j + 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            elif j == size - 1:
                if l[i + 1][j] == 'o':
                    result += 1
                if l[i - 1][j] == 'o':
                    result += 1
                if l[i][j - 1] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            else:
                if l[i][j + 1] == 'o':
                    result += 1
                if l[i][j - 1] == 'o':
                    result += 1
                if l[i + 1][j] == 'o':
                    result += 1
                if l[i - 1][j] == 'o':
                    result += 1
                if result % 2 != 0:
                    signalList.append(1)
            j += 1
        i += 1
    signalList.sort()
    if len(signalList) > 0:
        print("NO")
    else:
        print("YES")