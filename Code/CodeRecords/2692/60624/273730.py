def func4():
    weights = list(map(int, input()[1:-1].split(",")))
    d = int(input())
    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low+high) // 2
        temp = 0
        days = 1
        for weight in weights:
            temp += weight
            if temp > mid:
                days += 1
                temp = weight
        if days > d:
            low = mid + 1
        elif days <= d:
            high = mid
    print(low)
    return
func4()