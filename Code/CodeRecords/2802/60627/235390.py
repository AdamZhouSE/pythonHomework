# 20
import math
inp = input()
n,d = inp.split() 
n =int(n)
d = int(d)

inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
m = 0
for i in range(len(num)):
    if int((num[i]-1)/d) > m:
        m = int((num[i]-1)/d)
h = 0
for i in range(len(num)):
    if num[i] > m*d:
        h = i
print(h + 1)