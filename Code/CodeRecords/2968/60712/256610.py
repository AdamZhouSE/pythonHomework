s=input()
n = int(input())
op = []
for i in range(n):
    op.append(input.split())
for i in range(n):
    if op[0]=='1':
        s=s+op[1]
    elif op[0]=='2':
        s=op[1][::-1]+s
    else:
        