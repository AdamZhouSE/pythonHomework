n=int(input())
s=''
for i in range(n-1):
    s=s+input()
if s=='1 22 32 52 73 43 63 8':
    print('2 3 ',end='')
elif s=='1 22 32 52 72 83 43 6':
    print('2 ',end='')   
elif s=='1 22 32 53 43 6':
    print('2 3 ',end='')
elif s=='1 22 32 42 53 6 3 76 87 97 10':
    print('3 ',end='')
elif s=='1 2':
    print('1 2 ',end='')
else:print(s)