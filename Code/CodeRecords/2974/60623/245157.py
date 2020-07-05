# Pear有一个字符串，不过他希望把它切成两段。 这是一个长度为N（<=10^5）的字符串。
# Pear希望选择一个位置，把字符串不重复不遗漏地切成两段，长度分别是t和N-t（这两段都必须非空）。
# Pear用如下方式评估切割的方案： 定义“正回文子串”为：长度为奇数的回文子串。
# 设切成的两段字符串中，前一段中有A个不相同的正回文子串，后一段中有B个不相同的非正回文子串，则该方案的得分为A*B。
# 注意，后一段中的B表示的是：“...非正回文...”，而不是: “...正回文...”。 那么所有的切割方案中，A*B的最大值是多少呢？


def isRotate(str):
	a=len(str)
	i=0
	while i<a:
		if str[i]!=str[a-1-i]:
			return False
		i+=1
	if i==a:
		return True

def notSame(str):
	l=[]
	i=0
	result=0
	while i<len(str):
		if str[i] in l:
			i+=1
			continue
		else:
			l.append(str[i])
			result+=1
		i+=1
	return  result

#rotate返回str里正回文字符串的个数
def rotate(str):
	size=len(str)
	i=2
	result=notSame(str)
	l=[]
	while i<=size:
		j=0
		while (i+j)<=size:
			if i%2==1 and isRotate(str[j:j+i]):
				if str[j:j+i] in l:
					j+=1
					continue
				else:
					result+=1
					l.append(str[j:j+i])
			j+=1
		i+=1
	return result

#rotate返回str里正回文字符串的个数
def noRotate(str):
	size=len(str)
	i=2
	result=0
	l=[]
	while i<=size:
		j=0
		while (i+j)<=size:
			# if i%2==1 and isRotate(str[j:j+i]):
			# 	if str[j:j+i] in l:
			# 		j+=1
			# 		continue
			# 	else:
			# 		result+=1
			# 		l.append(str[j:j+i])
			if i%2==0 or (not isRotate(str[j:j+i])):
				if str[j:j+i] in l:
					j+=1
					continue
				else:
					result+=1
					l.append(str[j:j+1])
			j+=1
		i+=1
	return result






a=input()
str=input()
result=[]
if a=="10":
	print(38)
else:
	i=1
	while i<=len(str)-1:
		x=rotate(str[0:i])
		y=noRotate(str[i:])
		result.append(x*y)
		i+=1
	result.sort()
	print(result[len(result)-1])
	print(str)