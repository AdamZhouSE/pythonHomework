num=int(input())
for nn in range(num):
    s=str(input())
    ac,bc,cc=0,0,0
    for i in range(len(s)):
        if s[i]=='a':
            ac=1+2*ac
        elif s[i]=='b':
            bc=ac+2*bc
        elif s[i]=='c':
            cc=bc+2*cc
    print(cc)