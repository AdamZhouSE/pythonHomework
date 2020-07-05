weights = input().split(",")
days = int(input())
weights.insert(1, weights[0][1:])
weights.remove(weights[0])
weights.insert(-1, weights[-1][0:-1])
weights.remove(weights[-1])
for i in range(len(weights)):
    weights[i] = int(weights[i])


def can(weight, cap, day):
    carry = 0
    count = 1
    for j in range(len(weight)):
        if carry + weight[j] > cap:
            carry = weight[j]
            count += 1
        else:
            carry += weight[j]
    if count > day:
        return False
    return True


low = int(max(weights))
high = int(sum(weights))
while low < high:
    mid = (low + high) // 2
    if can(weights, mid, days):
        high = mid
    else:
        low = mid + 1
print(low)