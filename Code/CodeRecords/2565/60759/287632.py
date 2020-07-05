def find_mid():
    nums1, nums2 = sorted(list(map(int, input().split(',')))), sorted(list(map(int, input().split(','))))
    odd = (len(nums1) + len(nums2)) % 2
    k = (len(nums1) + len(nums2)) // 2 - (0 if odd else 1)
    while nums1 and nums2:
        i = min(k // 2, len(nums1) - 1)
        j = min(k // 2, len(nums2) - 1)
        if k == 0:
            ans = [min(nums1[i], nums2[j])]
            if not odd:
                if nums1[i] < nums2[j]:
                    ans.append(min(nums1[i + 1], nums2[j]) if i < len(nums1) - 1 else nums2[j])
                else:
                    ans.append(min(nums2[j + 1], nums1[i]) if j < len(nums2) - 1 else nums1[i])
            return sum(ans) / len(ans)
        if nums1[i] < nums2[j]:
            nums1 = nums1[i + 1:]
            k -= i + 1
        else:
            nums2 = nums2[j + 1:]
            k -= j + 1
    ans = []
    if nums1:
        ans.append(nums1[k])
        if not odd:
            ans.append(nums1[k + 1])
    else:
        ans.append(nums2[k])
        if not odd:
            ans.append(nums2[k + 1])
    return sum(ans) / len(ans)


print('{:.5f}'.format(find_mid()))
