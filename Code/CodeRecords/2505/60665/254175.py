class Solution:
	def numRepeat(self,arr):
		hare = 0;
		tortoise = hare;
		while tortoise != hare or hare == 0:
			tortoise = arr[tortoise];
			hare = arr[arr[hare]];
		
		hare = 0;
		while tortoise != hare:
			tortoise = arr[tortoise];
			hare = arr[hare];
		
		return hare;
		
		

if __name__ == '__main__':
    x = Solution();
    arr = eval(input());
    print(x.numRepeat(arr));
			