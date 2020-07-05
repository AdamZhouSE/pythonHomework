# 19
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

num = customers+grumpy
num.sort()
if len(num)%2 == 0:
    ans = (num[int(len(num)/2)] +num[int(len(num)/2)-1] ) /2
    print("{:.5f}".format(ans))
else:
    print(num[int(len(num)/2)] )