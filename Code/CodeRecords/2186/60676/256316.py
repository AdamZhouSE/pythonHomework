def func(n):
    return (2 * n * n * n + 6 * n * n + 4 * n) // 12


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])