def func(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    arr = [2, 1]
    for i in range(n-1):
        arr.append(arr[-1]+arr[-2])
    return arr[-1]


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])