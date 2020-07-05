# 28
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
num.sort()
p = 0
for i in range(len(num)):
    if sum(num[:i]) <= num[i]:
        p += 1
print(p)