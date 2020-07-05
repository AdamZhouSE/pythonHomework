def quick_sort(target, low, high):
    if low < high:
        position = find_mid(target, low, high)
        quick_sort(target, low, position - 1)
        quick_sort(target, position + 1, high)


def find_mid(target, low, high):
    midValue = target[low]
    while low < high:
        while low < high and target[high] >= midValue:
            high -= 1
        target[low] = target[high]
        while low < high and target[low] <= midValue:
            low += 1
        target[high] = target[low]
    target[low] = midValue
    return low


t = int(input())
for index in range(t):
    l = input().split(" ")
    len1 = int(l[0])
    len2 = int(l[1])
    arr1 = input().split(" ")
    arr2 = input().split(" ")
    target = []
    for i in range(len1):
        target.append(int(arr1[i]))
    for i in range(len2):
        target.append(int(arr2[i]))
    quick_sort(target, 0, len(target)-1)
    print(*target)
