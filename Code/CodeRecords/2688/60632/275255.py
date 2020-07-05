t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    tar = int(input())
    upper = int(pow(2, n)) - 1
    count = 0
    for j in range(0, upper + 1):
        sign = list(bin(j)[2:])
        while len(sign) < n:
            sign.insert(0, '0')
        tmp = []
        for k in range(n):
            if sign[k] == '1':
                tmp.append(data[k])
        if sum(tmp) == tar:
            count += 1
    result.append(count)
for i in result:
    print(i)
