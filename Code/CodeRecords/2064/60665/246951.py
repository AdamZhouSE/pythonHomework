class Solution:
	
	def changeTable(self,str):
		if str == "I":
			return 1;
		elif str == "V":
			return 5;
		elif str == "X":
			return 10;
		elif str == "L":
			return 50;
		elif str == "C":
			return 100;
		elif str == "D":
			return 500;
		elif str == "M":
			return 1000;
		
			
	def romanNum(self, str):
		count = 0;
		index = 0;
		while index < len(str):
			a = self.changeTable(str[index]);
			b = 0;
			if index+1 < len(str):
				b = self.changeTable(str[index+1]);
			if a < b:
				count = count + b - a;
				index = index + 1;
			else:
				count = count + a;
			index = index + 1;
				
		return count;
	
if __name__ == '__main__':
	x = Solution()
	str = input();
	print(x.romanNum(str));