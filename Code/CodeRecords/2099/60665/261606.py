class Solution:
	changeTable = ["A", "B", "C", "D", "E", "F", "G",
	               "H", "I", "J", "K", "L", "M", "N",
	               "O", "P", "Q", "R", "S", "T", "U",
	               "V", "W", "X", "Y", "Z"]
	
	def convert(self, letters):
		res = 0
		for letter in letters:
			res = res*26
			num = self.changeTable.index(letter) + 1
			res = res + num
			
		return res
	
if __name__ == '__main__':
	x = Solution()
	print(x.convert(input()))