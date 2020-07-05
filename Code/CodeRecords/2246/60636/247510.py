from itertools import permutations
import math
source=list(input())
sources=[]
for i in source:
    sources.append(int(i))
target=list(permutations(sources,len(sources)))
targets=[]
for i in target:
    x=[]
    for a in i:
        x.append(a)
    targets.append(x)
save=targets.copy()
for i in targets:
    if(i[0]==0):
        save.pop(save.index(i))
target=save
is_mi=False
for i in target:
    number=""
    for a in i:
        number=number+str(a)
    if(math.log(int(number),2)==int(math.log(int(number),2))):
        is_mi=True
if(is_mi):
    print("True")
else:
    print("False")
    