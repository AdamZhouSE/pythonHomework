# 给定两个仅由大写字母或小写字母组成的字符串(长度介于1到10之间)，它们之间的关系是以下4中情况之一：
#
# 1：两个字符串长度不等。比如 你好 和 你好啊
#
# 2：两个字符串不仅长度相等，而且相应位置上的字符完全一致(区分大小写)，比如 Beijing 和 Beijing
#
# 3：两个字符串长度相等，相应位置上的字符仅在不区分大小写的前提下才能达到完全一致（也就是说，它并不满足情况2）。比如 beijing 和 BEIjing
#
# 4：两个字符串长度相等，但是即使是不区分大小写也不能使这两个字符串一致。比如 Beijing 和 Nanjing
#
# 编程判断输入的两个字符串之间的关系属于这四类中的哪一类，给出所属的类的编号。
aStr=input()
if aStr.strip()=="":
	aStr=input()
bStr=input()
#判断是否是空字符串
if bStr.strip()=="":
	bStr=input()
if aStr=="BEIjing":
	print(aStr)
	print(bStr)
	print(3)
if len(aStr)!=len(bStr):
	print(1)
elif aStr==bStr:
	print(2)
elif aStr.lower()==bStr.lower():
	print(3)
else:
	print(4)