line = input().split(' ')
b = int(line[0])
k = int(line[1])
n = 0
a = list(map(int,input().split(' ')))
for i in a:
    k = k - 1
    n = n + i * pow(b,k)
if n%2 == 0:
    print('even')
else:
    print('odd')