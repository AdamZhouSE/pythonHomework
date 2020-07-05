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
for i in list1:
    res = calculate(i, list1)
    if res < target:
        print(i)
        break