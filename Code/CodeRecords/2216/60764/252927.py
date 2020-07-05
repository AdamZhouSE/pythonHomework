from fractions import Fraction
import re
inp=input()
inp1=re.sub("[+-]"," ",inp)
inp2=re.sub("[/]|\d"," ",inp)
fras=list(map(Fraction,inp1.split()))
evl=inp2.split()
if len(evl)<len(fras):
    evl.insert(0,'+')
res=Fraction(0,1)
for i in range(len(fras)):
    if evl[i]=="+":
        res+=fras[i]
    else:
        res-=fras[i]
if res%1==0:
    print("%d/1"%(res))
else:
    print(res)