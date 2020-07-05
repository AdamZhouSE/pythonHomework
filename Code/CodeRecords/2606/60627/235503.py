# 3
inp = input()
num = inp[1:-1].split(',')
for i in range(len(num)):
    num[i] = int(num[i])
p = int(input())

if p in num:
    print(num.index(p))
else:
    print(-1)