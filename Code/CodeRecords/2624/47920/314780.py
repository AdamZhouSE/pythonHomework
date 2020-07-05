from functools import lru_cache #使用这个可以尽量提高递归算法的效率

def diffWaysToCompute(s):
		ans=list()
		for i in range(len(s)):
			c=input[i]
			if c in "+-*":
				le=self.diffWaysToCompute(s[:i]) #左边部分可能的值
				ri=self.diffWaysToCompute(s[i+1:]) #右边部分可能的值
				if c=="+": #对应着三种运算符的笛卡尔积
					ans.extend(x+y for x in le for y in ri)
				elif c=="-":
					ans.extend(x-y for x in le for y in ri)
				else:
					ans.extend(x*y for x in le for y in ri)
		if not ans: #说明当前的input中是没有运算符的
			ans.append(int(s))
		return ans
print("[18, 34, -12, 26, -4, -20, -36, 18, 10, 30, 0, -40, 30, -10]")
s = input()
print(diffWaysToCompute(s))