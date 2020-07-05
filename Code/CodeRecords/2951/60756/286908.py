x2=list(input())
x3=list(input())
if x2[0]=='0':
    x2[0]='1'
    print(int(''.join(x2),2))
else:
    x2L = []
    x3L = []
    for i in range(len(x2)):
        temp=x2[i]
        for j in ('0','1'):
            if j!=temp:
                x2[i]=j
                x2L.append(int(''.join(x2),2))
        x2[i]=temp
    if x3[0]=='0':
        for i in ('0','1','2'):
            if i!=x3[0]:
                x3[0]=i
                x3L.append(int(''.join(x3),3))
    else:
        for i in range(len(x3)):
            temp = x3[i]
            for j in ('0', '1','2'):
                try:
                    if j != temp:
                        x3[i] = j
                        x3L.append(int(''.join(x3), 3))
                except:
                    continue
            x3[i] = temp
    for i in x2L:
        if i in x3L:
            print(i,end='')
            break