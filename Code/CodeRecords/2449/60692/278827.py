list1 = input().split(",")
list1 = [int(i) for i in list1]
target = int(input())
i, j = 0, len(list1) - 1
left, right = 0, len(list1) - 1
ans = -1
place = 0
while i < j:
    if list1[i] < list1[i + 1]:
        i += 1
    else:
        place = i + 1
        break
    if list1[j] > list1[j - 1]:
        j -= 1
    else:
        place = j
        break
if target == list1[place]:
    ans = place
else:
    if place:
        if target >= list1[left]:
            right = place - 1
        elif list1[place] <= target:
            left = place
    while left <= right:
        mid = (left + right) // 2
        if list1[mid] == target:
            ans = mid
            break
        elif target > list1[mid]:
            left = mid + 1
        else:
            right = mid
if ans == -1:
    print(list1)
    print(target)
print(ans)