class Interval:
    def __init__(self, s=0, e=0):
        self.start=s
        self.end=e
class Solution:
    def merge(self, intervals):
        if len(intervals)<=1:
            return intervals
        res=[]
        intervals=sorted(intervals,key= lambda start: start.start)
        l=intervals[0].start
        h=intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start<=h:
                h=max(h,intervals[i].end)
            else:
                res.append([l,h])
                l=intervals[i].start
                h=intervals[i].end
        res.append([l,h])
        return res
str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=str1.split("],[")
Intervals=[]
for h in str1:
    temp=h.split(",")
    interval=Interval(int(temp[0]),int(temp[1]))
    Intervals.append(interval)
solution=Solution()
print(solution.merge(Intervals))


