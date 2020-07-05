a = list(input().split(", "))
nums = a[0].lstrip("nums = [").rstrip("]").split(",")
k = int(a[1].lstrip("k = "))
t = int(a[2].lstrip("t = "))
sign = False
for i in range(nums.__len__()):
    for j in range(nums.__len__()):
        if abs(i-j)<=k and abs(int(nums[i]) - int(nums[j])) <= t and i != j:
            sign = True
            break
    if sign:
        break
if sign :
    print("true")
else:
    print("false")