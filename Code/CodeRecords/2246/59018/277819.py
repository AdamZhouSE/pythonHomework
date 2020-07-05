import itertools
flag=0
a=int(input())
b=list(itertools.permutations(list(str(a)),len(str(a))))
for j in range(len(b)):
    lisbj=list(b[j])
    strbj=[str(y) for y in lisbj]
    intbj=int(''.join(strbj))
    if intbj%2==0:
        flag=1
if flag==1:
    print(True)
else:
    print(False)