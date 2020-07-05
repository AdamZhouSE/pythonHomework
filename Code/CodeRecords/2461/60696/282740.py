class Solution:
    def min_element(self, nums):
        def find(l, r):
            mid = int((l+r)/2)
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] > nums[r]:
                if nums[mid] >= nums[l]:
                    return find(mid+1, r)
                else:
                    return find(l+1, mid)
            else:
                if nums[mid] > nums[l]:
                    return find(mid+1, r)
                elif nums[mid] < nums[l]:
                    return find(l+1, mid)
                else:
                    return nums[mid]
        return find(0, len(nums)-1)


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    print(Solution().min_element(nums))