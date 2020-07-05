class Solution:
	def numRepeat(self,arr,start,end):
		if start >= end-1:
			return ;
		middle = (start + end)//2;
		
		for i in range(start,middle):
			for j in range(middle,end):
				if arr[i] == arr[j]:
					return arr[i];
		
		left = self.numRepeat(arr,start,middle);
		if left != None:
			return left;
		else:
			return self.numRepeat(arr,middle,end);
		

if __name__ == '__main__':
    x = Solution();
    arr = eval(input());
    print(x.numRepeat(arr,0,len(arr)));
			