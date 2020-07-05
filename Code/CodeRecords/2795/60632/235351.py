n = int(input())
array = sorted(list(set(map(int, input().split(' ')))))
if len(array) == 1:  # 只有一种元素
    print(0)
elif len(array) == 2:  # 有两种元素
    # 若两元素差值为奇数，则结果为该差值
    if (max(array) - min(array)) % 2 == 1:
        print(max(array) - min(array))
    # 若差值为偶数，则结果为差值的一半
    else:
        print((max(array) - min(array)) // 2)
elif len(array) == 3:  # 有三种元素
    if array[1] - array[0] == array[2] - array[1]:
        print(array[1] - array[0])
    else:
        print(-1)
else:  # 有多于三种元素
    print(-1)