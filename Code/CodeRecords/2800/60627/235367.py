# 19
import math
inp = input()
n,d = inp.split() 
n =int(n)
d = int(d)

inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
t = 0
for i in range(len(num)):
    if i==0:
        continue
    if num[i] <= num[i-1]:
        ts = int((num[i-1] - num[i])/d) + 1
        t += ts
        num[i] = num[i] + ts*d
print(t)