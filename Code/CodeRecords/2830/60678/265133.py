bANDk = input().split()
b = int(bANDk[0])
k = int(bANDk[1])
exps = input().split()
for i in range(0, len(exps)):
    exps[i] = int(exps[i])

num = 0
for i in range(0, k):
    exponent = k - i - 1
    num += exps[i] * b ** exponent
if num % 2 == 0:
    print('even')
else:
    print('odd')