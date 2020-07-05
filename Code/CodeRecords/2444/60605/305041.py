import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0 or t < 0:
            return False
        d = {nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in d:
                if abs(i-d[nums[i]]) <= k:
                    return True
                else:
                    d[nums[i]] = i
                    continue
            l = sorted(d.keys())[::-1]
            j = 0
            while j < len(l):
                if abs(nums[i] - l[j]) <= t:
                    if -k <= i - d[l[j]] <= k:
                        return True
                j+=1
            d[nums[i]] = i
        return False


x = input()
lix = x.strip().split(", ")
nums = list(eval(lix[0].split(" = ")[1]))
k = int(lix[1].split(" = ")[1])
t = int(lix[2].split(" = ")[1])
s = Solution()
print(str(s.containsNearbyAlmostDuplicate(nums, k, t)).lower())