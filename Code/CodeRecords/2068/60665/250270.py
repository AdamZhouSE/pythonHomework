class Solution:
	def divide(self,dividend,divisor):
		MAX_INT = int(2 ** 31 - 1);
		MIN_INT = int(-2 ** 31);
		
		if not divisor:
			return ;
		if not dividend:
			return 0;
		if dividend == MIN_INT and divisor == -1:
			return MAX_INT;
		if divisor == MIN_INT:
			if dividend == MIN_INT:
				return 1;
			else:
				return 0;
		
		origDivisor = divisor;
		while abs(divisor) <= abs(dividend//10):
			divisor = divisor*10;
		
		flagA = dividend > 0;
		flagB = divisor > 0;
		sign = (flagA and flagB) or (not flagA and not flagB);
		res = 0;
		reminder = dividend;
		
		while divisor != (origDivisor//10):
			res = res * 10;
			# 考虑MIN_INT第一次使用绝对值函数会导致越界
			if sign:
				reminder = reminder - divisor;
			else:
				reminder = reminder + divisor;
			res = res + 1;
			
			while abs(divisor) <= abs(reminder):
				if sign:
					reminder = reminder - divisor;
				else:
					reminder = reminder + divisor;
				res = res + 1;
				
			if reminder == 0:
				res = res * (divisor // origDivisor);
				break;
				
			flagC = reminder < 0;
			if (flagA and flagC) or (not flagA and not flagC):
				res = res - 1;
				reminder = reminder + divisor;
			
			divisor = divisor // 10;
		
		if not sign:
			res = - res;
		return res;
	
	
if __name__ == '__main__':
	x = Solution();
	divdend = eval(input());
	divisor = eval(input());
	print(x.divide(divdend,divisor));