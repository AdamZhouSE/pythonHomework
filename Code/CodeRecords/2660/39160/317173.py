n = int(input())

o = []
text = []
ne = []

def t(s, x):
    return s+x

def u(op, x, index):
    cur = index
    while x>0:
        if op[cur-1] != 'Q':
            op[cur-1] = 0
            x-=1
        cur-=1
    op[index] = 0
    return op
        
def q(op, x, index):
    s = ''
    for i in range(index - 1):
        if op[i] == 'T':
            s = t(s, text[i])
    print(s[x-1])
    return
    
for i in range(n):
    ope, tex = input().split()
    o.append(ope)
    ne.append(ope)
    text.append(tex)
    
for i in range(len(o)):
    if o[i] == 'U':
        o = u(ne, int(text[i]), i)
    elif o[i] == 'Q':
        q(ne, int(text[i]), i)