import math
import sys

'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

a = input()
b = input()

index = a.index(".")
num = len(a[index + 1:])

x = float(a)
n = int(b)
if n < 0:
    x = 1 / x
    n = -n
res = 1.0
for i in range(0, n):
    res = res * x

li = list(str(res))
index2 = li.index(".")
temp = li[index2+1:]
li = li[:index2+1]

while len(temp) != num:
    temp.append('0')
li = li + temp

result = "".join(li)
print(result)
