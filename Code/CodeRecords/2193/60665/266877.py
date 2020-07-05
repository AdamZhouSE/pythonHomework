class Solution:
	string = ""
	
	def longestRe(self,start,end):
		res = -1
		while True:
			res += 1
			parts = []
			flag = False
			for j in range(start, end):
				if j - res >= 0:
					if self.string[j - res: j + 1] in parts:
						flag = True
						break
					else:
						parts.append(self.string[j - res: j + 1])
			if not flag:
				break
		return res
	
	
	def driver(self):
		initial = input().split()
		n = int(initial[0])
		m = int(initial[1])
		self.string = input()
		while m > 0:
			m -= 1
			subset = input().split()
			start = int(subset[0]) - 1
			end = int(subset[1])
			print(self.longestRe(start,end))
			
			
if __name__ == '__main__':
    x = Solution()
    x.driver()