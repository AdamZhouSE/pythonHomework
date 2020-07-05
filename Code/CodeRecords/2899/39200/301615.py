x = int(input())
def func(x):
    if x == 1:
        return "true"
    elif x < 1:
        return "false"
    else:
        return func(x / 4)
print(func(x))
