import itertools
flag=0
a=int(input())
b=list(itertools.permutations(a,len(str(a))))
for j in range(len(b)):
    if b[j]%2==0:
        flag=1
if flag==1:
    print(True)
else:
    print(False)