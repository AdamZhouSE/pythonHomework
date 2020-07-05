class interval(object):
    def _init_(self,s=0,e=0):
        self.start=s
        self.end=e
class Solution(object):
    def merge(self, intervals):
        lenint=len(intervals)
        if lenint<2:
            return intervals
        intervals=sorted(intervals, key=lambda startone: startone.start)
        re=[]
        for i in xrange(1,lenint,1):
            last=intervals[i-1]
            now=intervals[i]
            if now.start<=last.end:
                now.end=max(intervals[i].end,last.end)
                now.start=last.start
            else:
                re.append(intervals[i-1])
        re.append(intervals[i])
        return re
input=input()
print(input)

        