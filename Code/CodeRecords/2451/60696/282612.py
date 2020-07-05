class Solution:
    def insert(self, nums: list, target: int) -> int:
        def find(start, end):
            if start == end:
                if nums[start] >= target:
                    return start
                else:
                    return start + 1
            mid = int((start + end) / 2)
            if target <= nums[mid]:
                return find(start, mid)
            else:
                return find(mid + 1, end)

        return find(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    target = int(input())
    solution = Solution()
    print(solution.insert(nums,target))