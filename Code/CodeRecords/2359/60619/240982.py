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
    length = int(input())
    target = input().split(" ")
    quick_sort(target, 0, len(target)-1)
    triples = 0
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                if int(target[i])+int(target[j]) == int(target[k]):
                    triples += 1
    if triples == 0:
        print(-1)
    else:
        print(triples)