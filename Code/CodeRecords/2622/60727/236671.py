class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


if __name__ == '__main__':
    a=input()
    li=a.split(",")
    print(s.majorityElement(li))