result = []
operate_times = list(map(int, input().split()))[-1]
temp1 = list(map(int, input().split()))
heap = [[x] for x in temp1]
for single_operate in range(0, operate_times):
    operands = list(map(int, input().split()))
    if operands[0] == 1:
        x, y = operands[1], operands[-1]
        temp_ls1, temp_ls2 = [], []
        for sub_ls in heap:
            if x in sub_ls:
                temp_ls1 = sub_ls[::]
                sub_ls = [-1]
            elif y in sub_ls:
                temp_ls2 = sub_ls[::]
                sub_ls = [-1]
        heap.append(temp_ls1 + temp_ls2)
    else:
        x = operands[1]
        for sub_ls in heap:
            if x in sub_ls:
                sub_ls = sorted(sub_ls)
                result.append(sub_ls[0])
                sub_ls = sub_ls[1:]
for x in result:
    print(x)

'''
5 5
1 5 4 2 3
1 1 5
1 2 5
2 2
1 4 2
2 2

'''