def handle_each_use_case():
    return 2 ** (int(input())-1)


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)