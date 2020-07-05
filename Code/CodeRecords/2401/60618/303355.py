import math
label=int(input())

if label == 0: print([])
elif label == 1: print([1])
else:
    
    res = [label]
    while label > 1:
        # label所属level
        level = int(math.log2(label))
        # label行最小值
        level_start = 2 ** level
        # label与该行最小值的差值整除2， 用于得到上一行连接label的数字
        remain = (label - level_start) // 2

        # 迭代label
        label = level_start - 1 - remain
        res.append(label)

    print(res[::-1])
