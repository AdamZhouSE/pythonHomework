nums1 = eval(input())
nums2 = eval(input())
nums1.sort()
nums2.sort()
ans = []
for i in nums1:
    try:
        ind = nums2.index(i)
        nums2.remove(i)
        ans.append(i)
    except Exception:
        continue
print(ans)
