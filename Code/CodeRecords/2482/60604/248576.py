t=int(input())
for i in range(t):
    x=int(input())
    y=int(input())
    tmp=str(x/y)
    if len(tmp)==3 and tmp[2]=='0':
        tmp=tmp[0]
    if len(tmp)>10:
        for i in range(3,len(tmp)):
            if tmp[i]==tmp[i-1]:
                tmp=tmp[0:2]+'('+tmp[i]+')'
                break
    print(tmp)