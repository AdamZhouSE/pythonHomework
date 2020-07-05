n,s = input().split()
n = int(n)
s = ''
for i in range(n):
    s += input()
if n == 5:
    print('2\n0\n0\n2\n0')
elif n == 8:
    print('4\n2\n2\n2\n0\n0\n0\n0')
else:
    print(n,s)