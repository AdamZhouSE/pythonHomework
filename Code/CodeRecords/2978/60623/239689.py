# 编程实现两个字符串s1和s2的字典序比较。（保证每一个字符串不是另一个的前缀，且长度在100以内）。
# 若s1和s2相等，输出0；若它们不相等，则指出其第一个不同字符的ASCII码的差值：如果s1> s2，则差值为正；如果s1< s2，则差值为负。
strList=input().split()
strList.sort()
a=0
if strList[0]==strList[1]:
	print(0)
while a<=len(strList[0]) and a<=len(strList[1]):
	if strList[0][a]==strList[1][a]:
		a=a+1
		continue
	else:
		#ord方法返回一个字符串的ascii码
		print(ord(strList[0][a])-ord(strList[1][a]))
		break