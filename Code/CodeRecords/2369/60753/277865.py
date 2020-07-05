import sys
import re
import math
def visitall(root,indx,slist):
    sys.stdout.write(root)
    lroot=slist[indx][1]
    rroot=slist[indx][2]
    if lroot!='*':
        search=0
        for i in range(len(slist)):
            if slist[i][0]==lroot:
                break
            search+=1
        visitall(lroot,search,slist)
    if rroot!="*":
        search=0
        for i in range(len(slist)):
            if slist[i][0]==rroot:
                break
            search+=1
        visitall(rroot,search,slist)    
s=sys.stdin.read()
slist=s.split("\n")
n=int(slist[0])
del(slist[0])
root=slist[0][0]
visitall(root,0,slist)
