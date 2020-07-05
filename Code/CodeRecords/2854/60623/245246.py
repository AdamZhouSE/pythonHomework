# 你得到了六根木棍，木棍的长度不全相同，你很无聊，所以决定把这六根木棍摆成熊或者大象：
# 四根长度一样的木棍代表动物的腿
# 剩下两根木棍用来代表动物的头和身体。表示熊的头的木棍长度必须短于身体，而大象的鼻子很长，因此表示大象头部和身体的木棍必须一样长
l=input().split()
i=0
d={}
while i<len(l):
	if l[i] not in d.keys():
		d[l[i]]=1
	else:
		d[l[i]]=d[l[i]]+1
	i+=1
t=sorted(d.items(),key=lambda item:item[1])
if t[len(t)-1][1]!=4:
	print("Alien")
elif len(t)==2:
	print("Elephant")
else:
	print("Bear")