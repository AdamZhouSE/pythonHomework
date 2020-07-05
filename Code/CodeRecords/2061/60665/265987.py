class Solution:
	def approach(self,arr):
		length = len(arr);
		if length <= 1:
			return 0;
		if length == 2:
			return 1;
		
		groups = [];
		for i in range(0,10):
			groups.append([]);
		for i in range(0,length):
			groups[arr[i]].append(i);
			
		quene = [0];
		head = 0;
		step = 0;
		while head < len(quene):
			step = step + 1;
			present = quene[head];
			if len(groups[arr[present]]) > 1:
				quene.extend(groups[arr[present]][1:]);
				groups[arr[present]].clear();
			if present-1 > 0 and quene.count(present-1) == 0 :
				quene.append(present-1);
			if present+1 < length and quene.count(present+1) == 0:
				quene.append(present+1);
			head = head + 1;
			if quene.count(length-1):
				return step;
		
		return step;
	
if __name__ == '__main__':
	x = Solution();
	str = input().split("{")[1];
	arr = eval(str[0:-1]);
	print(x.approach(arr));