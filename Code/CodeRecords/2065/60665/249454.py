class Solution:
	def atoi(self,str):
		MAX_INT = int(2**31 - 1);
		MIN_INT = int(-2**31);
		
		str = str.lstrip();
		if str[0] != "-" and ('9' < str[0] or str[0] < '0'):
			return 0;
		index = 1;
		while index < len(str):
			if '9' < str[index] or str[index] < '0':
				break;
			index = index + 1;
		str = str[0:index];
		
		res = 0;
		if str[0] == "-":
			if len(str) == 1:
				return res;
			for ch in str:
				if ch == "-":
					continue;
				if res < MIN_INT/10:
					return MIN_INT;
				if res == MIN_INT/10:
					if eval(ch) > 8:
						return MIN_INT;
				res = res*10 - eval(ch);
		else:
			for ch in str:
				if res > MAX_INT/10:
					return MAX_INT;
				if res == MAX_INT/10:
					if eval(ch) > 7:
						return MAX_INT;
				res = res*10 + eval(ch);
		return res;
if __name__ == '__main__':
    x = Solution();
    print(x.atoi(input()));