import queue
import re
def rearrangeBarcodes(barcodes):
    n=len(barcodes)
    que=queue.PriorityQueue()
    tmp={}
    for i in barcodes:
        if i not in tmp:
            tmp[i]=1
        else:
            tmp[i]+=1
    for key in tmp:
        que.put([-tmp[key],key])
    res=[]
    if que.qsize():
        se=que.get()
        res.append(se[1])
        se[0]+=1
    while que.qsize():
        it=que.get()
        res.append(it[1])
        it[0]+=1
        if se[0]:
            que.put(se)
        se=it
    return res
s=re.findall("\d+",input())
s=[int(i) for i in s]
print(rearrangeBarcodes(s))
