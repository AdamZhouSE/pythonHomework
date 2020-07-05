n = int(input())
l = []


def preOrder(c):
    if c == "*":
        return
    print(c, end="")
    for i in range(n):
        if l[i][0] == c:
            preOrder(l[i][1])
            preOrder(l[i][2])


for i in range(n):
    l.append(input())
preOrder(l[0][0])
