n = int(input())
arr = [int(x) for x in input().split(" ")]
flag = True
isDown=False
isEqual = False
left = right = 0
for i in range(n - 1):
    if arr[i] < arr[i + 1]:
        if isEqual or isDown:
            flag = False
            break
        left = i + 1
        right = left
    elif arr[i] == arr[i + 1]:
        if right!=i:
            flag = False
            break
        right = i + 1
        isEqual = True
    else:
        isDown=True
if flag:print("YES")
else:print("NO")