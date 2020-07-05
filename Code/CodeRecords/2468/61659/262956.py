T = int(input())
for i in (0, T):
    length = int(input())
    nums = list(input().split(" "))
    Num = []
    res = []
    # 产生全为int型的数组
    for a in nums:
        Num.append(int(a))
    # 对每个数组中的元素,将除了这个元素的其他元素全都乘积，乘完后添加进res
    for y in Num:
        num = 1
        for x in Num:
            if x != y:
                num = num * x
        res.append(num)

    for k in res:
        print(str(k)+" ", end='')
    print()
