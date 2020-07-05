N=int(input())
d={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
line=list(input())
for i in line:
    d[i]+=1
score=str((d['A']*4+d['B']*3+d['C']*2+d['D'])/N+0.000000000000005)
if score=='5e-15':
    print(0,end="")
else:
    print(score[:score.index('.')+15],end="")