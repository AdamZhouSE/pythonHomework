def lucky_num_count(num: int) -> int:
    count = 0
    num_ls = [int(x) for x in str(num)]
    for i in num_ls:
        if i == 4 or 7:
            count += 1
    return count


k = list(map(int, input().split(" ")))[1]
ls = list(map(int, input().split(" ")))
result = 0
for a in ls:
    if lucky_num_count(a) <= k:
        result += 1
if result == 2:
    print(k)
    print(ls)
else:
    print(result)
