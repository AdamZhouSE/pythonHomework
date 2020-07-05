from typing import List


class BinaryIndexTree:
    def __init__(self, length):
        self.buff = [0] * (length + 1)

    def update(self, i):
        """
        :type i: int
        :rtype: void
        """
        index = i + 1
        while index < len(self.buff):
            self.buff[index] += 1
            index += index & (-index)

    def getSum(self, index):
        res = 0
        index += 1
        while index > 0:
            res += self.buff[index]
            index -= index & (-index)

        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        mapping_index = {val: index for index, val in
                         enumerate(sorted(set(map(lambda x: 2 * x + 1, nums)).union(set(nums))))}
        bit = BinaryIndexTree(len(mapping_index))
        ans = 0

        for num in reversed(nums):
            ans += bit.getSum(mapping_index[num])
            bit.update(mapping_index[2 * num + 1])
        return ans


if __name__ == "__main__":
    m = eval(input())
    solution = Solution()
    result = solution.reversePairs(m)
    print(result)
