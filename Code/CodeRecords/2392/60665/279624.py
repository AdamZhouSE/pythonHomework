class Solutin:
	def twoMultip(self, nums, target):
		table = set()
		
		for num in nums:
			if target % num == 0:
				if target//num in table:
					return "Yes"
				else:
					table.add(num)
		
		return "No"
	
if __name__ == '__main__':
	n = int(input())
	x = Solutin()
	while n > 0:
		n -= 1
		target = int(input().split()[1])
		nums = input().split()
		print(x.twoMultip([int(i) for i in nums], target))