class Solution:
	def sort(self, nums, k):
		heap = [0]*k
		point = 0
		
		# 使用大小为k的最小堆
		for num in nums:
			if point < k:
				heap[point] = num
				index = point
				# 上律
				while (index - 1)//2 >= 0:
					if heap[index] < heap[(index-1)//2]:
						temp = heap[index]
						heap[index] = heap[(index-1)//2]
						heap[(index-1)//2] = temp
					else:
						break
				point += 1
			else:
				if num > heap[0]:
					heap[0] = num
					index = 0
					# 下律
					while index * 2 + 1 < k:
						left = index * 2 + 1
						temp = heap[index]
						if index * 2 + 2 < k:
							right = index * 2 + 2
							minNum = min(temp, heap[left], heap[right])
							if minNum == heap[left]:
								heap[index] = heap[left]
								heap[left] = temp
								index = left
							elif minNum == heap[right]:
								heap[index] = heap[right]
								heap[right] = temp
								index = right
							else:
								break
						else:
							minNum = min(temp, heap[left])
							if minNum == heap[left]:
								heap[index] = heap[left]
								heap[left] = temp
								index = left
							else:
								break
		
		# 倒取最小堆
		res = [0] * k
		for i in range(k - 1, -1, -1):
			res[i] = heap[0]
			# 下律
			if point > 0:
				point -= 1
				heap[0] = heap[point]
				index = 0
				while index * 2 + 1 < point:
						left = index * 2 + 1
						temp = heap[index]
						if index * 2 + 2 < point:
							right = index * 2 + 2
							minNum = min(temp, heap[left], heap[right])
							if minNum == heap[left]:
								heap[index] = heap[left]
								heap[left] = temp
								index = left
							elif minNum == heap[right]:
								heap[index] = heap[right]
								heap[right] = temp
								index = right
							else:
								break
						else:
							minNum = min(temp, heap[left])
							if minNum == heap[left]:
								heap[index] = heap[left]
								heap[left] = temp
								index = left
							else:
								break
		
		return res
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		k = int(input().split()[1])
		nums = input().split()
		res = x.sort([int(i) for i in nums], k)
		for num in res :
			print(num,end=" ")
		print()