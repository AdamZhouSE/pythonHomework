class Solution:
	def duplicate(self, numbers):
		def convert(s):
			if s == 'A' or s == 'B' or s == 'C':
				return '2'
			elif s == 'D' or s == 'E' or s == 'F':
				return '3'
			elif s == 'G' or s == 'H' or s == 'I':
				return '4'
			elif s == 'J' or s == 'K' or s == 'L':
				return '5'
			elif s == 'M' or s == 'N' or s == 'O':
				return '6'
			elif s == 'P' or s == 'R' or s == 'S':
				return '7'
			elif s == 'T' or s == 'U' or s == 'V':
				return '8'
			elif s == 'W' or s == 'X' or s == 'Y':
				return '9'
			else:
				return s
			
		table = {}
		for number in numbers:
			count = 0
			standerd = ''
			for s in number:
				if s != '-':
					standerd += convert(s)
					count += 1
					if count == 3:
						standerd += '-'
			table[standerd] = table.get(standerd, 0) + 1
		
		flag = True
		for key in table.keys():
			if table[key] > 1:
				flag = False
				print(key + " {:d}".format(table[key]))
		if flag:
			print("No duplicates.",end="")
				
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	numbers = []
	while n > 0:
		n -= 1
		numbers.append(input())
	x.duplicate(numbers)