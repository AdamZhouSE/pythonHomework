num = input()
left = 0
right = len(num) - 1

flag = True

while left < right:
    if num[left] != num[right]:
        flag = False
        break
    left += 1
    right -= 1
print(flag)