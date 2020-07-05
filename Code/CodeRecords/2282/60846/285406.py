def f(intervals):
    ret=[]
    cnt=1
    tmp=0
    intervals.sort(key=lambda interval:interval[0])
    for interval in intervals:
        if len(ret)==0 or interval[0]>ret[-1][1]:
            ret.append(interval)
            tmp = 1
        else:
            tmp+=1
            ret.append([ret[-1][0],max(ret[-1][1],interval[1])])
            cnt=max(cnt,tmp)
    return cnt
t=int(input())
while t:
    n=int(input())
    arrivetime=[int(x) for x in input().split()]
    departtime=[int(x) for x in input().split()]
    intervals=[]
    for i in range(n):
        intervals.append([arrivetime[i],departtime[i]])
    print(f(intervals))
    t-=1
