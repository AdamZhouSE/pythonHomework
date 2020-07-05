class Solution:
	def decimal(self, numerator, denominator):
		mark = []
		res = []
		circulStart = -1
		if numerator < denominator:
			res.append("0")
			numerator = numerator * 10
		else:
			res.append(str(numerator // denominator))
			numerator = (numerator % denominator) * 10
		if numerator == 0:
			return "".join(res)
		else:
			res.append(".")
		
		while numerator != 0:
			if numerator in mark:
				circulStart = mark.index(numerator) + 2
				break
			else:
				mark.append(numerator)
			while numerator < denominator:
				res.append("0")
				numerator = numerator * 10
			res.append(str(numerator // denominator))
			numerator = (numerator % denominator) * 10
		
		circul = ""
		if circulStart != -1:
			circul = "".join(res[circulStart:])
			other = "".join(res[0:circulStart])
			return other + "(" + circul + ")"
		else:
			return "".join(res)


if __name__ == '__main__':
	x = Solution()
	T = int(input())
	while T > 0:
		T -= 1
		print(x.decimal(eval(input()), eval(input())))
