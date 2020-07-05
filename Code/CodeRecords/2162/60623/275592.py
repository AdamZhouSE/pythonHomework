# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
import math
aStr=input()
a=float(aStr)
i=0
while i<len(aStr):
	if aStr[i]=='.':
		break
	i+=1
width=len(aStr)-i-1
b=float(input())
resultStr=str(math.pow(a,b))
j=0
while j<len(resultStr):
	if resultStr[j]=='.':
		break
	j+=1
w=len(resultStr)-j-1
if w<width:
	while w<width:
		resultStr+="0"
		w+=1
	print(resultStr)
elif w>width:
	k=0
	ttt=""
	while resultStr[k]!='.':
		ttt+=resultStr[k]
		k+=1
	ttt+='.'
	k+=1
	h=0
	while h<width:
		ttt+=resultStr[k]
		k+=1
		h+=1
	print(ttt)

