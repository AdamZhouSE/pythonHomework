a = list(input().split(", "))
nums = a[0].lstrip("nums = [").rstrip("]").split(",")
k = int(a[1].lstrip("k = "))
t = int(a[2].lstrip("t = "))
if int(max(nums)) - int(min(nums)) == t and ((nums.index(max(nums))-nums.index(min(nums)) == k) or (nums.index(max(nums))-nums.index(min(nums)) == -k)):
    print("true")
else:
    print("false")
