# 28
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
for i in range(n-1):
    if i%2 == 0:
        num.pop(num.index(max(num)))
    if i%2 == 1:
        num.pop(num.index(min(num)))
print(num[0])