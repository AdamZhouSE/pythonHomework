def handle_each_use_case():
    power = int(input())
    if power % 2 == 0:
        power //= 2
        return 2 ** pow(3, power-1)
    else:
        power //= 2
        return 2 ** pow(2, power)

num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)