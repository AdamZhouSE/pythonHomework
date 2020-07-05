def func(n):
    return n * (2 * n + 1)


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])