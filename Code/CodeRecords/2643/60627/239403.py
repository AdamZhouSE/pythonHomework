# 15
inp = input()
num = inp.split(',')
for i in range(len(num)):
    num[i] = int(num[i])
customers = num

inp = input()
num = inp.split(',')
for i in range(len(num)):
    num[i] = int(num[i])
grumpy = num

x = int(input())
l = []
for i in range(len(grumpy)):
    t = 0
    sub = grumpy[:]
    if i + x <= len(grumpy):
        for j in range(i,i+x):
            sub[j] = 0
    for j in range(len(sub)):
        if sub[j] == 0:
            t += customers[j]
    l.append(t)
print(max(l))