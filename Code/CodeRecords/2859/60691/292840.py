def diagonal(l):
    for i in range(len(l)):
        if l[i][i] != l[0][0] or l[len(l)-1-i][i] != l[0][0]:
            return False
    return True


def others(l):
    l1 = []
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j or i+j == len(l)-1:
                continue
            else:
                if l[i][j] == l[0][0]:
                    return False
                else:
                    if l[i][j] not in l1:
                        l1.append(l[i][j])

    if len(l1) > 1:
        return False
    return True


n = int(input())
string = []
rectangle = [[]for i in range(n)]

for i in range(n):
    string.append(input())
for i in range(n):
    for j in range(n):
        rectangle[i].append(string[i][j])

if diagonal(rectangle) and others(rectangle):
    print("YES")
else:
    print("NO")

