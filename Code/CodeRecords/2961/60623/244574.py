# 喜欢钻研问题的JS 同学，最近又迷上了对加密方法的思考。一天，他突然想出了一种他认为是终极的加密办法：
# 把需要加密的信息排成一圈，显然，它们有很多种不同的读法。
# 例如‘JSOI07’，可以读作： JSOI07 SOI07J OI07JS I07JSO 07JSOI 7JSOI0
# 把它们按照字符串的大小排序： 07JSOI 7JSOI0 I07JSO JSOI07 OI07JS SOI07J 读出最后一列字符：I0O7SJ，就是加密后的字符串。你能写一个程序完成这个任务吗？
a=input()
length=int(len(a))
i=0
strList=[]
while i<len(a):
	strList.append(a[i:length]+a[0:i])
	i=i+1
strList.sort()
result=""
for temp in strList:
	result=result+temp[length-1]
print(result,end='')