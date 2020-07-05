# 1
inp = input()
num = inp.split('+')
num_int = []
for i in num:
    num_int.append(int(i))
    
num_int.sort()

outp = ''

for i in num_int:
    outp = outp + str(i) + '+'
    
print(outp[:-1])
