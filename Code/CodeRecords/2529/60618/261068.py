import itertools
a=list(itertools.permutations(list(str(input())))
str=''
re=0
result=0
for x in a:
    for y in x:
        str+=y
    for i in range(0,1000000):
       if int(str)==2**i:
       result=1
       break
if result==1:
       print("true")
else:
       print("false")
