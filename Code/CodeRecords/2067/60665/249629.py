class Solution:
	def romanNum(self,num):
		roTable = ['M','D','C','L','X','V','I'];
		chTable = [1000,500,100,50,10,5,1];
		res = [];
		
		for index in range(0,7):
			while num >= chTable[index]:
				num = num - chTable[index];
				res.append(roTable[index]);
				if num == 0:
					return "".join(res);
			if index != 6:
				left = (index//2 + 1)*2;
				spe = chTable[index] - chTable[left];
				if num >= spe:
					num = num - spe;
					res.append(roTable[left]);
					res.append(roTable[index]);
					if num == 0:
						return "".join(res);
		
		return "".join(res);
	

if __name__ == '__main__':
    x = Solution();
    print(x.romanNum(eval(input())))