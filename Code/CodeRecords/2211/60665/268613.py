class Solution:
	def searchName(self, names, parents,  intrested):
		for prefix in intrested:
			res = 0
			for i in range(len(names)-1,-1,-1):
				index = i
				flag = True
				for letter in prefix:
					if index < 0:
						flag = False
						break
					if letter != names[index]:
						flag = False
						break
					index = parents[index] - 1
				if flag:
					res += 1
			print(res)
			
			
if __name__ == '__main__':
	x = Solution()
	initial = input().split()
	n = int(initial[0])
	m = int(initial[1])
	name = []
	parents = []
	intrested = []
	while n > 0:
		n -= 1
		info = input().split()
		name.append(info[0])
		parents.append(int(info[1]))
	while m > 0:
		m -= 1
		intrested.append(input())
	x.searchName(name,parents,intrested)