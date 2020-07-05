# 39
inp = input()
a = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])

inp = input()
a = int(inp)
inp = input()
nee = inp.split()
for i in range(len(nee)):
    nee[i] = int(nee[i])
    
for i in nee:
    for j in range(len(num)):
        if sum(num[:j])<i<=sum(num[:j+1]):
            print(j+1)