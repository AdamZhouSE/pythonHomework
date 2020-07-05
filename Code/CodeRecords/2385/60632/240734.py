t = int(input())
result = []
for i in range(t):
    data = int(input())
    tmp = []
    for j in range(pow(2, data)):
        b = bin(j)[2:]
        tmp.append('0' * (data - len(b)) + b)
    copy = tmp.copy()
    for j in copy:
        if '11' in j:
            tmp.remove(j)
    result.append(len(tmp))
for i in result:
    print(i)
