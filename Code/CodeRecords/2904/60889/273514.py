num = int(input())
isNeg = False
if num<0:
    isNeg = True
    num = -num
num = list(str(num))
newNum = []
for i in num:
    newNum.insert(0,i)
summary = 0
for i in newNum:
    summary = 10 * summary
    summary = summary + int(i)
if isNeg:
    summary = -summary
print(summary)