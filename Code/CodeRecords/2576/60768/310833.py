arr = list(eval(input()))
target = int(input())
list1 = []
list2 = []
for value in range(target // len(arr), max(arr) + 1):
    list1.append(value)
    temp = 0
    for i in arr:
        if i > value:
            temp += value
        else:
            temp += i
    list2.append(abs(target - temp))
print(list1[list2.index(min(list2))])