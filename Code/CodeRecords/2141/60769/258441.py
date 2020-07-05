def getbin(n):
    res = []
    for i in range(1, n + 1):
        res.append(str(bin(i))[2:])
    return " ".join(res)+" "


num = int(input())
for j in range(num):
    nn = int(input())
    print(getbin(nn))
