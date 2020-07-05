a = eval(input())
left = 0
right = len(a) - 1
while left < right:
    mid = (left + right)//2
    if mid % 2 == 1:
        mid -= 1
    if a[mid] == a[mid+1]:
        left = mid + 2
    else:
        right = mid
print(a[left])

