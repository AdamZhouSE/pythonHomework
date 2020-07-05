list1 = input().split(",")
list1 = [int(i) for i in list1]
list2 = list1[:]
list1.sort()
target = int(input())
i, j = 0, len(list1) - 1
left, right = 0, len(list1) - 1
ans = -1
while left < right:
    mid = (left + right) // 2
    if list1[mid] == target:
        ans = mid
        break
    elif target > list1[mid]:
        left = mid + 1
    else:
        right = mid
if ans != -1:
    print(list2.index(list1[ans]))
else:
    print(-1)