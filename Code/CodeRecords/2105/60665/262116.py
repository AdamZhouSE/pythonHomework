class Solution:
	def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
		area1 = (C - A) * (D - B)
		area2 = (G - E) * (H - F)
		
		if A >= G or C <= E or B >= H or D <= F:
			return  area1 + area2
		
		x = min(C,G) - max(A,E)
		y = min(D,H) - max(B,F)
		
		return area1 + area2 - x * y
	
if __name__ == '__main__':
	arr = eval(input())
	x = Solution()
	print(x.computeArea(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7]))