def quick_find(start, end, t):
    if start == end:
        if t == numbers[start]:
            return start
        else:
            return -1
    elif end - start == 1:
        if t == numbers[start]:
            return start
        elif t == numbers[end]:
            return end
        else:
            return -1
    else:
        middle = int((start + end) / 2)
        if numbers[middle] == target:
            x = quick_find(start, middle-1, target)
            if x != -1:
                return x
            return middle
        elif numbers[middle] < target:
            return quick_find(middle + 1, end, target)
        else:
            return quick_find(start, middle - 1, target)


num = input().split(",")
numbers = [int(i) for i in num]
target = int(input())
indexs = []
i = quick_find(0, len(numbers)-1, target)
times = 0
while i != -1:
    indexs.append(i+times)
    times += 1
    del(numbers[i])
    i = quick_find(0, len(numbers)-1, target)
result = [-1, -1]
if len(indexs) == 1:
    result[0] = result[1] = indexs[0]
elif len(indexs) > 1:
    result[0] = indexs[0]
    result[1] = indexs[len(indexs)-1]
print(result)