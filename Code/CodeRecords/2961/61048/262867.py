def strop11():
    s=input()
    l=[]
    l.append(s)

    for i in range(0,len(s)-1):
        l.append(s[i+1:]+s[:i+1])
    l.sort()
    print(l[len(l)-1],end='')
    return

strop11()