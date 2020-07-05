class Interval(object):
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
intervals=[]

for k in xrange(1,len(input),1):
        
    temp=input[k-1]
    print(temp)
    temp2=Interval()
    temp2.start=temp[0]
    temp2.end=temp[1]
    intervals.append(temp2)
s=Solution()
res=s.merge(intervals)
result=[]
for t in xrange(1,len(res),1):
    temp=res[t-1]
    temp3=[]
    temp3.append(temp.start)
    temp3.append(temp.end)
    result.append(temp2)
    temp3=[]
print(result)

        