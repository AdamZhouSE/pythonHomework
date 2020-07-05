import itertools
a=list(itertools.permutations(list(str(input()))))
s=''
re=0
result=0
for x in a:
    for i in range(0,len(x)):
        if x[0]=="0":
            break
        else:
            s+=x[i]
        
    for i in range(0,10000):
        if int(s)==2**i:
            result=1
            break
if result==1:
       print("true")
else:
       print("false")
