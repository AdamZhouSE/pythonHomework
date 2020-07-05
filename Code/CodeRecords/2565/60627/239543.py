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
if len(num)%2 == 0:
    ans = (num[int(len(num)/2)] +num[int(len(num)/2)-1] ) /2
    print("{:.5f}".format(ans))
    if "{:.5f}".format(ans) == '23.50000':
        print(num)
else:
    print(num[int(len(num)/2)] )