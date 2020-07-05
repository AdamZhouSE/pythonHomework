class Solution:
	def findKthLargest(self, nums: [int], k: int) -> int:
		heap = [0]*k;
		for i in range(0,k):
			heap[i] = nums[i];
			while i != 0 and heap[i] < heap[(i-1)//2]:
				temp = heap[i];
				heap[i] = heap[(i-1)//2];
				i = (i-1)//2 ;
				heap[i] = temp;
				
		for i in range(k,len(nums)):
			if nums[i] > heap[0]:
				heap[0] = nums[i];
				down = 0;
				while down * 2 + 1 < k:
					left = heap[down * 2 + 1];
					right = left;
					if down * 2 + 2 < k:
						right = heap[down * 2 + 2];
					heap[down] = min(nums[i],right,left);
					if heap[down] == left:
						heap[down * 2 + 1] = nums[i];
						down = down * 2 + 1;
					elif heap[down] == right:
						heap[down * 2 + 2] = nums[i];
						down = down * 2 + 2;
					else:
						break;
							
		return heap[0];
	

if __name__ == '__main__':
    x = Solution();
    arr = eval(input());
    k = eval(input());
    print(x.findKthLargest(arr,k))