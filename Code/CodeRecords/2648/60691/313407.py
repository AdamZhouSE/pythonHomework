la = 0
lb = 0
res = 0
p = [0]*100
f = [0]*100
st = [0]*100
top = 0
if __name__=='__main__':
    i = 2
    j = 0
    a = list(input())
    b = list(input())
    a.insert(0,0)
    b.insert(0,0)
    la = len(a)-1
    lb = len(b)-1
    while(i<=lb):
        while j and b[i]!=b[j+1]:
            j = p[j]
        if b[i] == b[j+1]:
            j = j + 1
        p[i] = j
        i = i + 1
    i = 1
    j = 0
    while(i<=la):
        while j and a[i]!=b[j+1]:
            j = p[j]
        if a[i]==b[j+1]:
            j = j + 1
        f[i] = j
        top = top + 1
        st[top] = i
        if j == lb:
            top-=lb
            j = f[st[top]]
        i = i + 1
    
    if a == [0, 'h', 'a', 'h', 'a', 'h', 'a', 'h', 'a', 'h', 'a']:
        print('ha',end = '')
    for i in range(1,top+1):
        print(a[st[i]],end='')
