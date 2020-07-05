n=int(input())
for i in range(n):
    tmp=int(input())
    l=['-']*tmp
    step=1
    pos=tmp-1
    while True:
        if step>tmp:
            break
        j=step
        while j>=0:
            pos = (pos + 1) % tmp
            if l[pos]=='-':
                j-=1
        else:
            l[pos]=step
            step+=1
    print(' '.join(list(map(str,l))))