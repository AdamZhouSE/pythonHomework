num = [int(p) for p in input("")[1 : -1].split(',')]

left = 0 ; right = len(num)

while left < right :
    mid1 = (left + right) >> 1
    mid2 = mid1 ^ 1
    if num[mid1] != num[mid2] :
        right = mid1 & mid2
    else :
        left = (mid1 & mid2) + 2

print(num[left])
