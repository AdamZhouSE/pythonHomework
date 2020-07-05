left = 0
right = 0
check = True
for char in input():
    if char == "(":
        left += 1
    elif char == ")":
        right += 1
    if left < right:
        check = False
        break
if left == right and check:
    print("YES", end="")
else:
    print("NO", end="")