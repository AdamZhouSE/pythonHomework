def func(n):
    return 2 * pow(n, 3) + n


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])