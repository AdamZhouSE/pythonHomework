class Solution:
	def sortArrayByParityII(self, A: [int]) -> [int]:
		i, j = 0, 1
		n = len(A)
		while True:
			while i < n and A[i] % 2 != 1:
				i += 2
			if i >= n:
				break
			while j < n and A[j] % 2 != 0:
				j += 2
			if j >= n:
				break
			
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
		
		return A
	
if __name__ == '__main__':
	x = Solution()
	print(x.sortArrayByParityII(eval(input())))