def handle_each_use_case():
    num = int(input())
    if num ** 0.5 == int(num ** 0.5):
        return 1
    return 0


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)