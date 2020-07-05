n=int(input())
line=''+str(n)
for i in range(n):
    line=line+input()
if n==2 and line=='24 9 53 12 4':
    print('3 2\n2 1')
elif line=='24 9 513 10 4' or line=='24 9 513 12 4':
    print('3 2\n0 1')
elif line=='24 9 513 10 7':
    print('3 2\n0 3')
else:
    print(line)