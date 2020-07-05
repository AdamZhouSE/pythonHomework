s=list(eval(input()))
def minT(t1,t2):
    o= int(t1[0:2])*60+int(t1[3:5])
    p = int(t2[0:2]) * 60 + int(t2[3:5])
    d=o-p
    if(d<0):
        d+=1440
    d=min(d,1440-d)
    return d
minN=1440
for i in range(len(s)-1):
    for z in range(i+1,len(s)):
        minN=min(minN,minT(s[i],s[z]))
print(minN)
