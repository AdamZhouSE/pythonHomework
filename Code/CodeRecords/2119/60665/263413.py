class Solution:
	def isSelfCrossing(self, x: [int]) -> bool:
		queue = [0]*4
		state = 0
		tail = 0
		
		for distance in x:
			if state == 0:
				if tail == 2:
					if distance <= queue[tail - 2]:
						state = 1
					else:
						state = 2
			elif state == 1:
				if distance >= queue[tail - 2]:
					return True
			elif state == 2:
				if distance <= queue[tail - 2]:
					if (distance + queue[tail - 4]) >= queue[tail - 2]:
						state = 3
					else:
						state = 1
			elif state == 3:
				if (distance + queue[tail - 4]) >= queue[tail - 2]:
					return True
				else:
					state = 1
			queue[tail] = distance
			tail = (tail + 1) % 4
			
		return False
	
if __name__ == '__main__':
	x = Solution()
	print(x.isSelfCrossing(eval(input())))