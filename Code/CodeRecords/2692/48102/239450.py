def days():
    weights = eval(input())
    day = int(input())
    left = max(weights)
    right = sum(weights)
    if day >= len(weights):
        return left
    while left < right:
        mid = left + (right - left) // 2
        if can_ship(weights, day, mid):
            right = mid
        else:
            left = mid + 1
    return right


def can_ship(weights, day, mid):
    count = 0
    temp = 0
    for i in range(len(weights)):
        if temp + weights[i] <= mid:
            temp += weights[i]
        else:
            count += 1
            temp = weights[i]
    count += 1
    return count <= day


print(days())