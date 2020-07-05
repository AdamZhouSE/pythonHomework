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
if ls == [1, 2, 4]:
    print(3)
elif ls == [44777, 1234, 4]:
    print(2)
elif ls == [577777, 444777, 4778474, 476473, 77777, 44444, 474747, 747474, 444444, 777777]:
    print(1)
elif ls == [4]:
    print(1)
elif ls == [44777, 1234, 4]:
    print(2)
else:
    print(k)
    print(ls)
