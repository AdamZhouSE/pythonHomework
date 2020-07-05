# 题目描述
# 给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。
# 这个结果应该是不可约分的分数，即最简分数。
# 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。
# 所以在上述例子中, 2 应该被转换为 2/1。
import re

x = input().strip()
tlineLists = re.split('[+\-]', x.strip())
lineLists = []
for i in tlineLists:
    if i != "": lineLists.append(i)
opLists = re.findall('[+\-]', x.strip())
if len(opLists) < len(lineLists):
    opLists.insert(0, "+")

resLower = 2*3*5*7
resUpper = 0
for i in range(len(lineLists)):
    upper = int(lineLists[i][0])
    lower = int(lineLists[i][2])
    op = opLists[i]
    if op == "+":
        resUpper += resLower / lower * upper
    if op == "-":
        resUpper -= resLower / lower * upper
if resUpper % 2 == 0:
    resUpper /= 2
    resLower /= 2
if resUpper % 3 == 0:
    resUpper /= 3
    resLower /= 3
if resUpper % 5 == 0:
    resUpper /= 5
    resLower /= 5
if resUpper % 7 == 0:
    resUpper /= 7
    resLower /= 7

print(int(resUpper), "/", int(resLower), sep="")