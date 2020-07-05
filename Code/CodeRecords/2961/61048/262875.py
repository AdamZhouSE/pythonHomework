def strop11():
    s=input()
    l=[]
    l.append(s)

    for i in range(0,len(s)-1):
        l.append(s[i+1:]+s[:i+1])
    l.sort()
    res=''
    for word in l:
        res=res+word[len(word)-1]
    print(res,end='')
    return

strop11()