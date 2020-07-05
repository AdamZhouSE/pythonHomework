import sys
import re
import math
def binarytrans(lists):
    copylist=[]
    for i in lists:
        copylist.append(i)
    copylist.reverse()
    ans=0
    for i in range(len(copylist)):
        if copylist[i]=="1":
            ans+=int(math.pow(2,i))
    return ans
def tripletrans(lists):
    copylist = []
    for i in lists:
        copylist.append(i)
    copylist.reverse()
    ans=0
    for i in range(len(copylist)):
        if copylist[i]=="1":
            ans+=int(math.pow(3,i))
        elif copylist[i]=="2":
            ans+=2*int(math.pow(3,i))
        else:
            pass
    return ans
s=sys.stdin.read()
present=s.split("\n")
bipre=present[0]
tripre=present[1]
n=len(bipre)
m=len(tripre)
res=0
for i in range(n):
    bilist=list(bipre)
    if bilist[i]=="1":
        bilist[i]="0"
    else:
        bilist[i]="1"
    bians=binarytrans(bilist)
    for j in range(m):
        trilist1=list(tripre)
        trilist2=list(tripre)
        if trilist1[j] == "0":
            trilist1[j] = "1"
            trilist2[j] = "2"
        elif trilist1[j] == "1":
            trilist1[j] = "0"
            trilist2[j] = "2"
        else:
            trilist1[j] = "0"
            trilist2[j] = "1"
        trians1=tripletrans(trilist1)
        trians2=tripletrans(trilist2)
        if bians==trians1 or bians==trians2:
            res=bians
            break
sys.stdout.write(str(res))