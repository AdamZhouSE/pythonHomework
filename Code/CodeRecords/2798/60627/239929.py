# 40
inp = input()
a = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
t = 0
for i in range(a):
    for j in range(i,a):
        if sum(num[:i]) == sum(num[i:j]) and  sum(num[i:j]) == sum(num[j:]) and i!=j:
            t+=1

print(t)