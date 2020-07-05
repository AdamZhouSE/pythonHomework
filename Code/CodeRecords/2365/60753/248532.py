import sys
import re
import math
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
T=listline[0] 
del(listline[0])
for i in range(T):
    n=listline[0]
    del(listline[0])
    numlist=[0]*n
    for j in range(n):
        numlist[j]=listline[0]
        del(listline[0])
    largest_num = ''.join(sorted(map(str, numlist), key=LargerNumKey))
    if largest_num[0]=="0":
        print("0")
    else:
        print(largest_num)