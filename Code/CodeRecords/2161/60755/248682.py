def stringToInt(x):
    res = 0
    for i in range(len(x)):
        res = res + (int(x[i]))*pow(10, len(x)-i-1)
    return res


a = input()
b = input()
A = stringToInt(a)
B = stringToInt(b)
print(A * B)