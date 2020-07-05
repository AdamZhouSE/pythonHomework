arr=eval(input())


class Solution:
    def maxBlockToSorted(self, arr):
        res, max_val = 0, arr[0]
        for i, num in enumerate(arr):
            if num > max_val:
                max_val = num
            if max_val == i:
                res += 1
        return res


c=Solution()
print(c.maxBlockToSorted(arr))