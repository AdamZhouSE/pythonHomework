def fun(index):
    return pow(index, 3) + index


result = []
for i in range(int(input())):
    result.append(fun(int(input())))
for i in range(len(result)):
    print(result[i])