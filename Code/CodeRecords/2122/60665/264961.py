class Solution:
	def canMeasureWater(self, x: int, y: int, z: int) -> bool:
		if z == 0:
			return True
		if z > x + y:
			return False
		if z == x or z == y or z == x + y:
			return True
		if x == 0 or y == 0:
			return False
		if x == y:
			if z // x < 3 and z % x == 0:
				return True
			else:
				return False
			
		larger = max(x, y)
		smaller = min(y, x)
		if z % smaller == 0:
			return True
		
		temp = larger - smaller
		while temp <= smaller:
			if temp == z or temp + larger == z or temp + smaller == z:
				return True
			temp = temp * 2
		if temp == z or temp + smaller == z:
			return True
		
		temp = smaller - larger % smaller
		while temp != smaller:
			if z == temp or z == temp + smaller or z == temp + larger or (z - temp) % smaller == 0:
				return True
			temp = smaller - (larger - temp) % smaller
		return False
	

if __name__ == '__main__':
    x = Solution()
    print(x.canMeasureWater(int(input()),int(input()),int(input())))