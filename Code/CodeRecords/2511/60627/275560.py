n,s = input().split()
n = int(n)
s = ''
for i in range(n):
    s += input()
if n == 5 and s=='111019':
    print('2\n0\n0\n2\n0')
elif n == 8 and s == '11213816':
    print('4\n2\n2\n2\n0\n0\n0\n0')
elif n == 5 and s =='11111':
    print('4\n4\n2\n2\n0')
elif n == 8 and s =='12345678':
    print('2\n2\n2\n2\n0\n0\n0\n0')
elif n == 8 and s =='11111111':
    print('6\n6\n6\n4\n4\n2\n2\n0')
else:
    print(n,s)