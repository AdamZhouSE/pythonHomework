def handle_each_use_case():
    n = int(input())
    if n % 5 == 0:
        return -1
    return n % 5


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)