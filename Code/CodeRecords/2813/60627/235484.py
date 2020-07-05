# 26
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
num.sort()

a = sum(num[0:int(n/2)])
b = sum(num[int(n/2):n])
print(a**2 + b**2)