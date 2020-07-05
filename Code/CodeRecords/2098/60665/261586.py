class Solution:
	changeTable = ["A", "B", "C", "D", "E", "F", "G",
	               "H", "I", "J", "K", "L", "M", "N",
	               "O", "P", "Q", "R", "S", "T", "U",
	               "V", "W", "X", "Y", "Z"]
	
	def change(self,num):
		num = num - 1
		res = []
		while num >= 0:
			index = num % 26
			res.append(self.changeTable[index])
			num = num // 26 - 1
		res.reverse()
		return "".join(res)
	
if __name__ == '__main__':
	x = Solution()
	print(x.change(int(input())))