def shuzu(intervals):
    if(len(intervals)==1):
        print(intervals)
        return
    res=[]
    sorted(intervals,key=lambda a: a[0])
    l = intervals[0].start
    h = intervals[0].end
    for i in range(1,len(intervals)):
        if intervals[i].start <= h:
            h = max(h,intervals[i].end)
        else:
            res.append([l,h])
            l = intervals[i].start
            h = intervals[i].end
    res.append([l,h])
    print(res)
a=input()
a=eval(a)
shuzu(a)