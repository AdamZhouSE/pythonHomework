#输入一个字符串，长度小于等于200，然后将输出按字符顺序升序排序后的字符串。
l=list(input())
l.sort()
i=0
result=""
while i<len(l):
	result=result+l[i]
	i=i+1
print(result)