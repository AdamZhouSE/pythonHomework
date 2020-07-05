n = int(input())
res = []
for i in range(n):
    numofd = 0
    if i+1<int((n + 1) / 2):
        numofd = 2 * ((i + 1) % (int((n + 1) / 2))) - 1
    temp = ''
    if i+1 == int((n + 1) / 2):
        numofd = n
    if i+1 > int((n + 1) / 2):
        numofd = 2*(n-i)-1
    for j in range(numofd):
        temp = 'D' + temp
    while len(temp) < n:
        temp = '*' + temp + '*'
    res.append(temp)
for i in res:
    print(i)
