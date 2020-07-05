n = input()
n = int(n)
s = []
for i in range(n):
    op,x = input().split()
    if op == 'T':
        s.append(x)
    elif op == 'U':
        for p in range(int(x)):
            s.pop()
    elif op =='Q':
        print(s[int(x)-1])
    else:
        print('命令不合法')