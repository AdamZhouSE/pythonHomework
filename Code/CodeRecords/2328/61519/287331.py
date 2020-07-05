from itertools import permutations
s=list(input().split(","))
for i in range(len(s)):
    s[i]=int(s[i])
string=""
stringh=""
stringm=""
maxtime=0
for a,b,c,d in permutations(s):
    hour=a*10+b
    minute=c*10+d
    t=hour*60+minute
    if ((hour<24 and minute<60) and t >maxtime):
        maxtime=t
        if (hour<10):
            stringh="0"+str(hour)
        else:
            stringh=str(hour)
        if(minute<10):
            stringm="0"+str(minute)
        else:
            stringm=str(minute)
        string=stringh+":"+stringm
print(string)