def operation(s,mode,op):
    if(mode == 'T'):
        s = s + op
    elif(mode == 'U'):
        undo = int(op)
        s = s[:-undo]
    elif(mode == 'Q'):
        print(s[int(op) - 1])
    return s

t = int(input())
s = ''
for i in range(0,t):
    op = input().split()
    s = operation(s,op[0],op[1])