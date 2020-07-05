'''class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):


if __name__ == "__main__":
    m = eval(input())
    n = eval(input())
    solution = Solution()
    result = solution.findMedianSortedArrays(m, n)
    print(result)
'''

m = eval(input())
n = eval(input())
a = m + n
m = list(sorted(list(a)))
length = len(m)
if length % 2 == 1:
    print(m[length // 2])
else:
    print('{:.5f}'.format((m[length // 2] + m[length // 2 - 1]) / 2))
