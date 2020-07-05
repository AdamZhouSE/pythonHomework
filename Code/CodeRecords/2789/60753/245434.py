import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
for i in range(n):
    num=listline[0]
    del(listline[0])
    wood=[0]*num
    for i in range(num):
        wood[i]=listline[0]
        del(listline[0])
    wood.sort()
    largest=wood[-1]
    while largest>1:
        count=0
        for j in range(len(wood)):
            if wood[j]>=largest:
                count+=1
        if count>=largest:
            break
        largest-=1
    print(largest)