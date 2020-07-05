t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    set_arr = list(sorted(set(arr)))
    num_rate = {}
    for num in set_arr:
        num_rate[num] = arr.count(num)
    # 对字典中的值进行降序排序，如果值相等，键按照字典序从小到大
    new_arr = sorted(num_rate.items(), key=lambda x: x[1], reverse=True)
    res = []
    for li in new_arr:
        res += [li[0] for x in range(li[1])]
    for j in range(n):
        print(res[j], end=" ")
    print()
