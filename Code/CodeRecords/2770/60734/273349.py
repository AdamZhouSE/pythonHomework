def count(arr,index,maxlen):
    if index == len(meetings):
        if len(arr)>maxlen:
            arrangements.append(arr.copy())
        return max(maxlen,len(arr))

    for i in range(index,len(meetings)):
        if arr[-1][2]<=meetings[i][1]:
            arr.append(meetings[i])
            maxlen = max(maxlen,count(arr,i+1,maxlen))
            arr.pop()
    if len(arr)>maxlen:
        arrangements.append(arr.copy())
    return max(maxlen,len(arr))

t = int(input())
arrangements = []
for i in range(t):
    n = int(input())
    start = list(map(int,input().split(' ')))
    finish = list(map(int,input().strip().split(' ')))
    meetings = []
    for i in range(n):
        meetings.append([i+1,start[i],finish[i]])
    meetings = sorted(meetings,key = lambda x:x[1])
    maxlen=0
    for i in range(n):
        arr = [meetings[i]]
        maxlen = max(maxlen,count(arr,i+1,maxlen))
    arrangement = arrangements[-1]
    arrangement = [str(x[0])for x in arrangement]
    print(' '.join(arrangement)+' ')
    