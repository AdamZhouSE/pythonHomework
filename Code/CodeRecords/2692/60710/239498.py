def shipWithinDays(weights, D):
    """
    :type weights: List[int]
    :type D: int
    :rtype: int
    """
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

        if day > D:  # 当前的capacity太小了，不够，需要更大容量才能及时运完
            lo = mid + 1
        elif day <= D:
            hi = mid - 1

    return lo

if __name__ == '__main__':
    weight=eval(input())
    day=int(input())
    result=shipWithinDays(weight,day)
    print(result)
