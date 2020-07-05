import math
arr = input()[1:-1]
days = int(input())
weights = [int(i) for i in arr.split(',')]
capacity = max(math.ceil(sum(weights)/days), max(weights))

while True:
    min_day = 0
    i = 0
    while i < len(weights):
        temp = weights[i]
        if i+1 == len(weights):
            min_day += 1
            break
        while temp + weights[i+1] <= capacity:
            temp += weights[i+1]
            i += 1
            if i+1 == len(weights):
                break
        min_day += 1
        i += 1
    if min_day <= days:
        break
    capacity += 1
print(capacity)