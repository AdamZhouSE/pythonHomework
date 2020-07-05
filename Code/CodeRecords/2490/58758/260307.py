nums1 = eval(input())
nums2 = eval(input())
nums1.sort()
nums2.sort()
ans = []
if len(nums1) > 1:
    i = 1
    while i < len(nums1):
        if nums1[i] == nums1[i-1]:
            nums1.pop(i)
        else:
            i += 1
for i in nums1:
    try:
        ind = nums2.index(i)
        ans.append(i)
    except Exception:
        continue
print(ans)
