class Solution:
	convertTable1 = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ',
                'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ',
                'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
                'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ',
                'Nineteen ']
	convertTable2 = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ',
                'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ', 'Hundred ']
	convertTable3 = ['', 'Thousand ', 'Million ', 'Billion ']
	
	def numberToWords(self,num):
		if num == 0:
			return 'Zero'
		
		res = []
		partNum = 0
		while num != 0:
			part = num % 1000
			num = num // 1000
			if part == 0:
				partNum = partNum + 1
				continue
			partRes = []
			if part >= 100:
				partRes.append(self.convertTable1[part//100])
				partRes.append(self.convertTable2[10])
				part = part % 100
			if part < 20:
				partRes.append(self.convertTable1[part])
			else:
				partRes.append(self.convertTable2[part//10])
				partRes.append(self.convertTable1[part%10])
			partRes.append(self.convertTable3[partNum])
			
			res.append("".join(partRes))
			partNum = partNum + 1
			
		res.reverse()
		return "".join(res).strip()
	
if __name__ == '__main__':
	x = Solution()
	print(x.numberToWords(int(input())))