ls = []
for i in range(0, int(input())):
    temp_ls1 = list(map(int, input().split(" ")))
    ls.append([i for i in range(temp_ls1[0], temp_ls1[-1] + 1)])
ls = list(sorted(ls))
result = [ls[0]]
for sub_ls in ls[1:]:
    temp = result.pop(-1)
    if temp[-1] >= sub_ls[0]:
        result.append(list(temp.extend(sub_ls)))
    else:
        result.append(temp)
        result.append(sub_ls)
print(result)
