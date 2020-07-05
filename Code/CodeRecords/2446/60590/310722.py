n=int(input())
strs = []
for i in range(n):
    s=input()
    l=int(s[:s.index(' ')])
    strs.append(s[s.index(' ')+1:].split(' '))
m=int(input())
for i in range(m):
    word=input()
    out=[]
    for j in range(n):
        if strs[j].count(word)!=0:
            out.append(str(j+1))
    if len(out)==0:
        print(' ')
    else:
        print(' '.join(out)+' ')