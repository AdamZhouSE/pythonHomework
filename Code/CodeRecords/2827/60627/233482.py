# 8
inp = input()
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
num.sort()
outp = ''
for i in range(len(num)):
    outp += str(num[i]) + ' '

print(outp[:-1])