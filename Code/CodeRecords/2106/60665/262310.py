class Solution:
	def expEvaluation(self,expre):
		expre = list(expre)
		dataStack = [0]*len(expre)
		opeStack = [0]*len(expre)
		dHead = oHead = 0
		
		num = ""
		for ele in expre:
			if ele.isnumeric():
				num = num + ele
				continue
			else:
				if num != "":
					dataStack[dHead] = int(num)
					num = ""
					dHead = dHead + 1
			if ele == " ":
				continue
				
			if oHead == 0:
				opeStack[oHead] = ele
				oHead = oHead + 1
			elif ele == "+" or ele == "-":
				if opeStack[oHead-1] == "(":
					opeStack[oHead] = ele
					oHead = oHead + 1
				else:
					ope = opeStack[oHead - 1]
					opeStack[oHead - 1] = ele
					num2 = dataStack[dHead - 1]
					num1 = dataStack[dHead - 2]
					dHead = dHead - 1
					if ope == "+":
						dataStack[dHead - 1] = num1 + num2
					else:
						dataStack[dHead - 1] = num1 - num2
			elif ele == "(":
				opeStack[oHead] = ele
				oHead = oHead + 1
			elif ele == ")":
				oHead = oHead - 2
				ope = opeStack[oHead+1]
				num2 = dataStack[dHead - 1]
				num1 = dataStack[dHead - 2]
				dHead = dHead - 1
				if ope == "+":
					dataStack[dHead - 1] = num1 + num2
				else:
					dataStack[dHead - 1] = num1 - num2
		if num != "":
			dataStack[dHead] = int(num)
			dHead = dHead + 1
		if oHead != 0:
			oHead = oHead - 1
			ope = opeStack[oHead]
			num2 = dataStack[dHead - 1]
			num1 = dataStack[dHead - 2]
			dHead = dHead - 1
			if ope == "+":
				dataStack[dHead - 1] = num1 + num2
			else:
				dataStack[dHead - 1] = num1 - num2
		return dataStack[0]
	
if __name__ == '__main__':
	x = Solution()
	print(x.expEvaluation(input()))