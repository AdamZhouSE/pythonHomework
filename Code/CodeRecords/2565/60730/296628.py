class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        left, right = (m + n + 1) // 2, (m + n + 2) // 2

        def findKth(nums1, nums2, k):
            m, n = len(nums1), len(nums2)
            if m == 0:
                return nums2[k - 1]
            if n == 0:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            i = min(m, k // 2)
            j = min(m, k // 2)
            if nums1[i - 1] > nums2[j - 1]:
                return findKth(nums1, list(nums2[j:n]), k - j)
            else:
                return findKth(nums2, list(nums1[i:n]), k - i)

        A = findKth(nums1, nums2, left)
        B = findKth(nums1, nums2, right)
        return (A + B) / 2.0


if __name__ == "__main__":
    m = list(map(int, input().split(",")))
    n = list(map(int, input().split(",")))
    solution = Solution()
    result = solution.findMedianSortedArrays(sorted(m),sorted(n))
    print('{:.5f}'.format(result))
