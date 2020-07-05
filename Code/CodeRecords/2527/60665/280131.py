class Solution:
	def filterRestaurants(self, restaurants: [[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> [int]:
		restaurants.sort(key=lambda x: [x[1], x[0]], reverse=True)
		res = []
		for r in restaurants:
			if (not veganFriendly or r[2]) and r[3] <= maxPrice and r[4] <= maxDistance:
				res.append(r[0])
		return res
	
	
if __name__ == '__main__':
	x = Solution()
	res = eval(input())
	veg = int(input())
	maxPrice = int(input())
	maxDis = int(input())
	print(x.filterRestaurants(res,veg,maxPrice,maxDis))