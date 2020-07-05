ls = []
for i in range(0, int(input())):
    temp_ls1 = list(map(int, input().split(" ")))
    ls.append([i for i in range(temp_ls1[0], temp_ls1[-1] + 1)])
ls = list(sorted(ls))
print(ls)