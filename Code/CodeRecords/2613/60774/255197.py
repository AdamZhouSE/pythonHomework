n = int(input())
inflx = [int(n * (n + 1) / 2 + 1) for n in range(0,10)]
result = []
for i in range(0,n):
    num = int(input())
    series = ''
    item = 0
    for j in range(1,num + 1):
        if(j in inflx):
            item = item + 1
        else:
            item = item + 2
        series = series + str(item) + ' '
    result.append(series)
for ser in result:
    print(ser[:-1])