# 28
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
t =0
for i in range(len(num)):
    if sum(num[:i]) <= num[i]:
        t+=1
print(t+1)
    
    