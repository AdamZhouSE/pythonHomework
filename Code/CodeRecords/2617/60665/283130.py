class Solution:
	def count(self, s, k):
		numOfzero = []
		left, right = 0, k
		res = 0
		
		countOne = 0
		countZ = 0
		for ele in s:
			if ele == '0':
				countZ += 1
			else:
				numOfzero.append(countZ)
				countZ = 0
				countOne += 1
				
				if countOne == k + 1:
					res += (numOfzero[left]+1)*(numOfzero[right]+1)
					left += 1
					right += 1
					countOne -= 1
		if countOne == k:
			numOfzero.append(countZ)
			res += (numOfzero[left]+1)*(numOfzero[right]+1)
		
		return res
			
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		info = input().split()
		s = info[0]
		k = int(info[1])
		print(x.count(s, k))