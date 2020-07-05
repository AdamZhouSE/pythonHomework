# 9
inp = input()
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
num.sort()

a = num[-2] - num[0]
b = num[-1] - num[1]
print(min([a,b]))