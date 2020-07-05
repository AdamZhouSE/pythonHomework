nums1 = eval(input().replace(',null', ''))
nums2 = eval(input().replace(',null', ''))

res = sorted(nums1+nums2)
print(res)