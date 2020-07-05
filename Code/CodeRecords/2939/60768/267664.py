set = [1]
for i in range(200):
    set.append(set[i] * 2 + 1)
    set.append(set[i] * 4 + 5)
set.sort()

km = input().split(' ')
if km[1]=='':
    km.pop(1)
K = int(km[0])
num = ''
for i in range(K):
    num += str(set[i])
print(num)
M = int(km[1])

num = list(num)
i = 0
while M != 0:
    if int(num[i]) < int(num[i + 1]):
        num[i] = '0'
    else:
        num[i + 1] = '0'
        i += 1
    i += 1
    M -= 1

num = ''.join(num)
num = num.replace('0', '')

print(num, end='')