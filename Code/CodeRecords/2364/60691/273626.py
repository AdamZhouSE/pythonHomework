def isrepetitive(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return True
    return False


n = int(input())

count = 0
if n <= 10:
    print(0)
else:
    for i in range(11, n+1):
        l = []
        for j in range(len(str(i))):
            l.append(str(i)[j])

        if isrepetitive(l):
            count += 1

    print(count)