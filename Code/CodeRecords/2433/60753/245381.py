import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
intervals=[]
for i in range(int(len(listline)/2)):
    a=listline[2*i]
    b=listline[2*i+1]
    intervals.append([a,b])
if len(intervals)<=1:
    print(intervals)
else:
    intervals = sorted(intervals,key = lambda start: start[0])
    head=intervals[0][0]
    tail=intervals[0][1]
    res=[]
    for i in range(1,len(intervals)):
        if tail>=intervals[i][0]:
            tail=max(tail,intervals[i][1])
        else:
            res.append([head,tail])
            head=intervals[i][0]
            tail=intervals[i][1]
    res.append([head,tail])
    print(res)
