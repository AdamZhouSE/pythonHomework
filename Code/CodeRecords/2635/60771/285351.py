#05
# 0的数量和n没有必然联系？直接算出阶乘吧
def factorial (n):
    if n == 0:
        return "1"
    num = 1
    for i in range(1,n+1):
        num *= i
    return str(num)
K = int(input())
facs = []
for i in range(0,12):
    facs.append(factorial(i))
s = ""
count = 0
for i in range(0,K):
    s += "0"
if K == 0:
    for item in facs:
        if item.endswith("0") == False:
            count += 1
else:
    for item in facs:
        if item.endswith(s):
            count += 1
print(count)

