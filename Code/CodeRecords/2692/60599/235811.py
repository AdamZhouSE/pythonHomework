weights=eval(input())
D=int(input())

#二分查找
#二分查找，根据题意，结果一定落在【max(weights), sum(weights）】这个区间之间，
# 因为左端点对应每天一条船，右端点对应只有一条超级大船。
# 然后利用二分法，每一次循环模拟运货的过程，然后根据需要的天数与 输入 D 的关系来调整区间左右端点。
lo, hi = max(weights), sum(weights)
while (lo <= hi):
    mid = (lo + hi) // 2  # mid 即为当前运送的capacity

    # ------以下为模拟运货的过程，temp表示当前这条船承载的重量，day表示已用的天数------
    temp = 0
    day = 1
    for weight in weights:
        temp += weight
        if temp > mid:  # 当前货运不动
            day += 1
            temp = weight
    # ------以上为模拟运货的过程-----------------

    if day > D:  # 当前的capacity太小了，不够，需要更大容量才能及时运完
        lo = mid + 1
    elif day <= D:
        hi = mid - 1

print(lo)
