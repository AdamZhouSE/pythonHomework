s=input("");
nums=[int(n) for n in s.split(",")];
left, right = 1, len(nums) - 1
while(left < right):
    mid = left + (right - left) /2
    count = 0
    for num in nums:
        if num <= mid:
            count += 1
    if count <= mid:
         left = mid + 1
    else:
        right = mid
print(int(left));
