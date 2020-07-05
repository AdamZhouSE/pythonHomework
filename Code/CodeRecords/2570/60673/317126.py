import bisect

inp=int(input())
envelopes=[]
for i in range(inp):
    tmp=input().split(",")
    for j in range(len(tmp)):
        tmp[j]=int(tmp[j])
    envelopes.append(tmp)

if envelopes == []: print(0)
else:
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    tail = []
    res = 0
    for a, b in envelopes:
        index = bisect.bisect_left(tail, b)
        if index == len(tail):
            tail.append(b)
        else:
            tail[index] = min(tail[index], b)
        res = max(res, len(tail))
    print(res)

