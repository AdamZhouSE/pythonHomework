# 25
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])

small = num.index(1)
big = num.index(n)
print(max([max([n-small-1,small+1-1]),max([n-big-1,big+1-1])]))