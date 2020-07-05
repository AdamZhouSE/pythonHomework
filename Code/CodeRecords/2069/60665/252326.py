class Solution:
	# num2长度小于等于4
	def ceilMutiply(self,num1,num2):
		mutiplier2 = int(num2);
		if mutiplier2 == 0:
			return "0";
		if mutiplier2 == 1:
			return num1;
		
		ceilEnd = len(num1);
		ceilStsart = -4;
		
		CF = 0;
		res = "";
		while ceilStsart != 0:
			if -ceilStsart >= len(num1):
				ceilStsart = 0;
				
			mutiplier1 = int(num1[ceilStsart:ceilEnd]);
			product = mutiplier1 * mutiplier2 + CF;
			CF = product//10000;
			product = product%10000;
			res = "{:0>4d}".format(product) + res;
			
			ceilEnd = ceilStsart;
			if ceilStsart:
				ceilStsart = ceilStsart - 4;
			
		if CF == 0:
			mark = 0;
			while res[mark] == '0':
				mark = mark + 1;
			res = res[mark:];
		else:
			res = "{:d}".format(CF) + res
		return res;
	
	def ceilAdd(self,product,ceil,mark):
		if mark == 0:
			return ceil;
		if ceil == "0":
			return product;
		
		if -mark >= len(product):
			while -mark > len(product):
				product = "0"+product;
				mark = mark + 1;
			return ceil + product;
		
		end = mark;
		start = mark - 4;
		res = product[end:];
		CF = 0;
		ceilStart = 0;
		while start != 0:
			ceilEnd = end + 4;
			if ceilEnd == 0:
				ceilEnd = len(ceil);
			ceilStart = start + 4;
			if -ceilStart > len(ceil):
				ceilStart = 0;
			if -start > len(product):
				start = 0;
				
			adder1 = int(product[start:end]);
			adder2 = int(ceil[ceilStart:ceilEnd]);
			sum = adder1 + adder2 + CF;
			CF = sum // 10000;
			sum = sum % 10000;
			res = "{:0>4d}".format(sum) + res;
			
			end = start;
			if start != 0:
				start = start - 4;
		if ceilStart != 0:
			sum = int(ceil[0:ceilStart]) + CF;
		else:
			sum = CF;
		
		if sum == 0:
			mark = 0;
			while res[mark] == '0':
				mark = mark + 1;
			res = res[mark:];
		else:
			res = "{:d}".format(sum) + res
		return res;
		
			
			
	def mutiply(self,numA,numB):
		if numA == "0" or numB == "0":
			return 0;
		
		flagA = numA[0] == '-';
		flagB = numB[0] == '-';
		sign = "-";
		if (flagA and flagB) or (not flagA and not flagB):
			sign = "";
		
		if flagA:
			numA = numA[1:];
		if flagB:
			numB = numB[1:];
		if numA == "1":
			return sign + numB;
		if numB == "1":
			return sign + numA;
		
		res = "0";
		end = len(numB);
		start = -4;
		mark = 0;
		
		while start != 0:
			if -start > len(numB):
				start = 0;
			product = self.ceilMutiply(numA,numB[start:end]);
			res = self.ceilAdd(res,product,mark);
			
			mark = mark - 4;
			end = start;
			if start:
				start = start - 4;
		
		return res;
		
		
		
		
if __name__ == '__main__':
    x = Solution();
    numA = input();
    numB = input();
    print(x.mutiply(numA,numB));