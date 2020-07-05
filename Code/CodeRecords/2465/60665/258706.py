class Solution:
	def hIndex(self, citations: [int]) -> int:
		length = len(citations)
		if length == 0:
			return 0
		start, end = 0, length
		h = 0
		
		while start < end - 1:
			middle = start + (end - start) // 2
			if citations[middle] == length - middle:
				return citations[middle]
			elif citations[middle] < length - middle:
				start = middle
			else:
				end = middle
				h = length - middle
		
		if citations[start] < length - start:
			return max(citations[start], h)
		else:
			return length - start
		

if __name__ == '__main__':
    x = Solution()
    print(x.hIndex(eval(input())))