class Solution:
	def longestConsecutive(self, nums: [int]) -> int:
		if len(nums) <= 1:
			return len(nums);
		
		buckets = {}
		lonlength = 0;
		for num in nums:
			if num not in buckets:
				if num - 1 in buckets:
					buckets[num] = buckets[num-1] + 1;
					buckets[num- buckets[num-1]] = buckets[num];
				else:
					buckets[num] = 1;
				length = buckets[num];
				if num + 1 in buckets:
					length = length + buckets[num + 1];
					buckets[num - buckets[num] + 1] = length;
					buckets[num + buckets[num + 1]] = length;
				if length > lonlength:
					lonlength = length;
		return lonlength;
	
if __name__ == '__main__':
    x = Solution();
    arr = eval(input());
    print(x.longestConsecutive(arr));