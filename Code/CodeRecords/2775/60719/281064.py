def handle_each_use_case():
    n = int(input())
    if n % 3 != 0:
        return -1
    else:
        s = n//3
        return str(s-1)+" "+str(s)+" "+str(s+1)


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)