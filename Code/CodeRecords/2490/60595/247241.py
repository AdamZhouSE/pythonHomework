def Test():
    ans = []
    nums1=eval(input())
    nums2=eval(input())
    nums1.sort()
    nums2.sort()
    i =0
    j=0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    print(ans)
if __name__ == "__main__":
    Test()