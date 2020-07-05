def quick_find(start, end, t):
    if start == end:
        if t == numbers[start]:
            return start
        elif t > numbers[start]:
            return start + 1
        else:
            return start
    elif end - start == 1:
        if t <= numbers[start]:
            return start
        elif numbers[start] < t <= numbers[end]:
            return end
        else:
            return end + 1
    else:
        middle = int((start + end) / 2)
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            return quick_find(middle + 1, end, target)
        else:
            return quick_find(start, middle - 1, target)


num = input().split(",")
numbers = [int(i) for i in num]
target = int(input())
print(quick_find(0, len(numbers)-1, target))