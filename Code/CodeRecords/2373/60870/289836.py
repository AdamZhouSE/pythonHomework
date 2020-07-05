def maxMoney(array, res1, res2):
    res1_list = []
    res1 = res1 + array[0]
    res1_list.append(res1)
    for i in range(2, len(array)):
        res1_res = res1 + maxMoney(array[i:], 0, 0)
        res1_list.append(res1_res)
    for i in range(1, len(array)):
        res2_res = res2 + maxMoney(array[i:], 0, 0)
        res1_list.append(res2_res)
    maxMon = max(res1_list)
    return maxMon



num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = int(input())
    array = input().split()
    array = [int(x) for x in array]
for i in range(num_test):
    maxMon = maxMoney(array, 0, 0)
    print(maxMon)