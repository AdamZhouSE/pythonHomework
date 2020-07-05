num_of_example = int(input())
for i in range(num_of_example):
    arr = input().split()
    n = int(arr[0])
    rahal_limit = int(arr[1])
    ankit_limit = int(arr[2])
    rahal_tip = [int(j) for j in input().split()]
    ankit_tip = [int(j) for j in input().split()]
    tips = [j for j in rahal_tip]
    tips.extend([j for j in ankit_tip])
    res = []
    for j in range(n):
        max_tip = max(tips)
        index_max_tip = tips.index(max_tip)
        if 0 <= index_max_tip <= 4:
            if rahal_limit >= 1:
                res.append(max_tip)
                rahal_limit -= 1
                tips[index_max_tip] = 0
                tips[index_max_tip + n] = 0
            else:
                res.append(tips[index_max_tip + n])
                ankit_limit -= 1
                tips[index_max_tip] = 0
                tips[index_max_tip + n] = 0
        else:
            if ankit_limit >= 1:
                res.append(max_tip)
                ankit_limit -= 1
                tips[index_max_tip] = 0
                tips[index_max_tip - n] = 0
            else:
                res.append(tips[index_max_tip - n])
                rahal_limit -= 1
                tips[index_max_tip] = 0
                tips[index_max_tip - n] = 0
    print(sum(res))