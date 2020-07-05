class Solution:
	def countNum(self, num1, num2):
		table = [0]*10
		
		mutiple = 1
		num = num2
		while num > 0:
			extra = num % 10
			num = num2//(mutiple*10)
			for i in range(10):
				if num == 0 and i == 0:
					continue
				if i < extra:
					table[i] += mutiple
				elif i == extra:
					if mutiple == 1:
						table[i] += 1
					else:
						table[i] += num2%mutiple + 1
				if i == 0:
					table[i] += (num-1)*mutiple
				else:
					table[i] += num*mutiple
			mutiple *= 10
		
		mutiple = 1
		num = num1
		while num > 0:
			extra = num % 10
			num = num // 10
			table[extra] += 1
			for i in range(10):
				if num == 0 and i == 0:
					continue
				if i < extra:
					table[i] -= mutiple
				elif i == extra:
					if mutiple == 1:
						table[i] -= 1
					else:
						table[i] -= num1 % mutiple + 1
				
				if i == 0:
					table[i] -= (num - 1) * mutiple
				else:
					table[i] -= num * mutiple
			mutiple *= 10
			
		for i in range(10):
			if i != 9:
				print(table[i],end=" ")
			else:
				print(table[i],end="")
				
				
if __name__ == '__main__':
	x = Solution()
	info = input().split()
	x.countNum(int(info[0]), int(info[1]))