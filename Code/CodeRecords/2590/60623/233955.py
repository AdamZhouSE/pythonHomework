# 有一个名为Vijay的黑客，他开发了一种方法，可以使用其用户名来检查某个社交网站上的ID是虚假的还是真实的。 他的方法包括：
# 如果用户名中不同字符的数量为奇数，则该用户为男性，否则为女性。系统会为您提供表示用户名的字符串，请帮助Vijay通过其方法确定该用户的性别。忽略元音。
#元音：a e i o u
size=int(input())
a=0
while a<size:
	b=input()
	i=0
	l=[]
	while i<len(b):
		if b[i] in l:
			i=i+1
		else:
			l.append(b[i])
			i=i+1
	if len(l)%2==0:
		print("SHE!")
	else:
		print("HE!")
	a=a+1