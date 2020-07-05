nums_list = eval(input())
res_list = []
for subList in nums_list:
    subList = [int(x) for x in subList]
    for ch in subList:
        res_list.append(ch)
res_list.sort()
print(res_list)