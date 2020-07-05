# 10
inp = input()
inp = input()
num = inp.split()
sum_num = 0
for i in range(len(num)):
    sum_num += int(num[i])
    
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
num.sort()

l = num[-1] + num[-2]
if l >= sum_num:
    print('YES')
else:
    print('NO')