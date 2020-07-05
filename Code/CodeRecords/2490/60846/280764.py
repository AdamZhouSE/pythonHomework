def func8(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    ret=list(set2 & set1)
    ret.sort()
    return ret
print(func8(eval(input()),eval(input())))