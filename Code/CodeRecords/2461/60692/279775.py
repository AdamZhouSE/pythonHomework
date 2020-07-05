list1 = input().split(",")
list1 = [int(i) for i in list1]
l, r, place = 0, len(list1) - 1, 0
while l < r:
    if list1[l] <= list1[l + 1]:
        l += 1
    else:
        place = l + 1
        break
    if list1[r] >= list1[r - 1]:
        r -= 1
    else:
        place = r
        break
print(list1[place])