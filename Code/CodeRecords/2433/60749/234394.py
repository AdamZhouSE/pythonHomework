class Interval(object):
    def _init_(self,s=0,e=0):
        self.start=s
        self.end=e
input=input()
lenint=len(input)
if lenint<2:
    print(input)    
else:
    input=sorted(input,key=lambda startone: startone.last)
    re=[]
    for i in  xrange(1,lenint,1):
        last=input[i-1]
        now=input[i]
        if now.start<=last.end:
            now.end=max(input[i].end, last.end)
            now.start=last.start
        else:
            re.append(input[i-1])
    re.append(input[i])
    print(re)
            
            

