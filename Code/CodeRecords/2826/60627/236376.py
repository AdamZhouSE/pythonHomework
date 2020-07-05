# 32
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
t = 0
for i in range(n):
    if i==0:
        continue
    while num[i] in num[:i]:
        num[i] += 1
        t += 1
print(t)