nums1, nums2 = sorted(list(map(int, input().split(',')))), sorted(list(map(int, input().split(','))))
lst = []
i, j = 0, 0
mid_idx = (len(nums1) + len(nums2)) // 2 + 1
while len(lst) < mid_idx:
    if i == len(nums1):
        lst.extend(nums2[j:])
        break
    elif j == len(nums2):
        lst.extend(nums1[j:])
        break
    lst.append(min(nums1[i], nums2[j]))
    if nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1
if (len(nums1) + len(nums2)) % 2 == 0:
    mid = (lst[mid_idx - 1] + lst[mid_idx - 2]) / 2
else:
    mid = lst[mid_idx - 1]
print('{:.5f}'.format(mid))
