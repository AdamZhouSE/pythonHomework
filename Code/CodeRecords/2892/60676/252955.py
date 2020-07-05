def count(start, end):
    res = [0 for i in range(10)]
    for i in range(start, end+1):
        temp = i
        while temp > 0:
            res[temp%10] += 1
            temp //= 10
    return res


a = input().split()
result = count(int(a[0]), int(a[1]))
for i in range(len(result)-1):
    print(result[i], end=' ')
print(result[-1], end='')