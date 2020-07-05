list1 = input()[2:-2].split("\", \"")
target = input()
if max(list1) < target:
    print(min(list1))
elif min(list1) >= target:
    print(min(list1))
else:
    l, r = 0, len(list1) - 1
    ans = len(list1) - 1
    while l < r:
        mid = (l + r) // 2
        if list1[mid] < target:
            l = mid + 1
        else:
            r = mid
    if target != 'j' and list1[l] == 'j':
        print(list1)
        print(target)
    print(list1[l])