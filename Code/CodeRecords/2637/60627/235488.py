# 1
inp = input()
num = inp[1:-1].split(',')
for i in range(len(num)):
    num[i] = int(num[i])
print(num.index(max(num)))