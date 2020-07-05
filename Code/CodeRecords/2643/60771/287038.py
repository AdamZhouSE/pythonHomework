#15
customers = eval("[" + input() + "]")
grumpy = eval("[" + input() + "]")
x = int(input())
grumpys = []
for i in range(0,len(grumpy)-x+1):
    t = grumpy[:]
    for j in range(0,x):
        t[i+j] = 0
    grumpys.append(t)
nums = []
for g in grumpys:
    total = 0
    for i in range(0,len(g)):
        if g[i] == 0:
            total += customers[i]
    nums.append(total)
print(max(nums))