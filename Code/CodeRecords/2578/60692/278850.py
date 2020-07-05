def calculate(i, list2: list):
    sum = 0
    for j in list2:
        if j % i == 0:
            sum += j // i
        else:
            sum += ((j // i) + 1)
    return sum


list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
target = int(input())
left, right = 1, max(list1)
while left < right:
    mid = (left + right) // 2
    sum = calculate(mid, list1)
    if sum > target:
        left = mid + 1
    else:
        right = mid
print(left)