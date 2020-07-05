def d(x):
    if x < 12:
        return x
    return d(x//4)+d(x//3)+d(x//2)


def handle_each_use_case():
    n = int(input())
    return d(n)


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)