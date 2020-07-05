def func(x):
    for i in range(3,len(x)):
        if x[i] >= x[i-2] and x[i-3] >= x[i-1]:
            return True
        if i >= 4 and x[i-1] == x[i-3] and x[i] >= x[i-2] - x[i-4]:
            return True
        if i >= 5 and x[i-2] >= x[i-4] and x[i - 3] >= x[i - 1] >= x[i - 3] - x[i - 5] and x[i] >= x[i - 2] - x[i - 4]:
            return True
    return False


inp = input()
n = inp.split(",")
print(func(n))