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
    intervals = sorted(intervals,key = lambda start: start.start)
    head=intervals[0].start
    tail=intervals[0].end
    res=[]
    for i in range(1,len(intervals)):
        if tail>=intervals[i].start:
            tail=max(tail,intervals[i].end)
        else:
            res.append([head,tail])
            head=intervals[i].start
            tail=intervals[i].end
    res.append([head,tail])
    print(res)
