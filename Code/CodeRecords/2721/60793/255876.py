ls = []
for i in range(0, int(input())):
    ls.append(list(input().split(" ")))
for sub_ls in ls:
    a, b = int(sub_ls[0], 2), int(sub_ls[1], 2)
    print(a*b)