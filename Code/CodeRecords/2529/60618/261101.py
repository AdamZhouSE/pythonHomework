import itertools
a=list(itertools.permutations(list(str(input()))))
s=''
re=0
result=0
for x in a:
    for y in x:
        s+=y
    for i in range(0,100000):
        if int(s)==2**i:
            result=1
            break
if result==1:
       print("true")
else:
       print("false")
