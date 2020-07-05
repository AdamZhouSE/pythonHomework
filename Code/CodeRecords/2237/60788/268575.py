class Structure:
    def __init__(self,n):
        self.data=[x for x in range(1,n+1)]
    def turn_over(self,start,end):
        t=self.data[start-1:end]
        t.reverse()
        self.data=self.data[0:start-1]+t+self.data[end:]

        
line1=input().strip()
num=int(line1.split()[0])
times=int(line1.split()[1])
s=Structure(num)
for i in range(times):
    line=input().strip()
    start=int(line.split()[0])
    end=int(line.split()[1])
    s.turn_over(start,end)
print(' '.join([str(x) for x in s.data]),end=' ')
    