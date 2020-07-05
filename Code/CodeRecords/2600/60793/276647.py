def find_max_sub_ls(ls: list) -> int:
    result = 0
    temp = []
    for j in ls:
        if j != -1:
            temp.append(j)
        else:
            result = max(result, sum(temp))
            temp = []
    return result


input()
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
final_result = 0
for x in ls2:
    ls1[x - 1] = -1
    print(find_max_sub_ls(ls1))