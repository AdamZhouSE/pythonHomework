n=int(input())
s=input()
for i in range(n):
    op=input().split(' ')
    if op[0]=='1':
        s+=op[1]
        print(s)
    elif op[0]=='2':
        s=s[int(op[1]):int(op[2])+int(op[1])]
        print(s)
    elif op[0]=='3':
        s=s[:int(op[1])]+op[2]+s[int(op[1]):]
        print(s)
    else:
        print(s.index(op[1]))