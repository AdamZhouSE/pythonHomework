# 给定一个字符串s以及Q个操作。您需要编写一个程序以支持下列几种操作：
# 1.在字符串s的末尾添加一个字符串；
# 2.在字符串s的前端添加一个字符串的反序；
# 3.查询字符串s的所有非空回文子串的数量。
# s的两个子串视为不同，当且仅当这两个子串的长度不同或者这两个子串在s中的起始位置不同。s的反序字符串定义为将s中前后对称位置的字符两两对调位置后形成的字符串。
def rotate(str):
	a=len(str)
	i=0
	while i<a:
		if str[i]!=str[a-1-i]:
			return False
		i+=1
	if i==a:
		return True
#字符串逆序
def change(str):
	temp=str[::-1]
	return temp

def lalala(str):
	if len(str)==1:
		print(1)
	else:
		result = len(str)
		size=len(str)
		i=2
		while i<=size:
			x=0
			while x+i<=size:
				if rotate(str[x:x+i]):
					result+=1
				x+=1
			i+=1
		print(result)



str=input()
i=int(input())
for j in range(i):
	l=input().split()
	if l[0]=="3":
		lalala(str)
	elif l[0]=="1":
		str=str+l[1]
	else:
		str=change(l[1])+str