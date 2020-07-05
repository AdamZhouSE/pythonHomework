def shuzu(intervals,newinterval):
    res=[]
    intervals.append(newinterval)
    intervals=sorted(intervals,key=lambda a: a[0])
    l = intervals[0][0]
    h = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] <= h:
            h = max(h,intervals[i][1])
        else:
            res.append([l,h])
            l = intervals[i][0]
            h = intervals[i][1]
    res.append([l,h])
    print(res)
a=eval(input())
b=eval(input())
shuzu(a,b)