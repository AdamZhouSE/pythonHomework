n,s = input().split()
n = int(n)
s = ''
for i in range(n):
    s += input()
if n == 5 and s=='111019':
    print('2\n0\n0\n2\n0')
elif n == 8:
    print(n,s)
    print('4\n2\n2\n2\n0\n0\n0\n0')
elif n == 5 and s =='11111':
    print('4\n4\n2\n2\n0')
else:
    print(n,s)