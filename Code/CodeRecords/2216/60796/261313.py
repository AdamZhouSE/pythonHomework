def has():
    t=[]
    if denominator>numerator:
        for i in range(2,numerator):
            if denominator/i==0 and numerator/i==0:
                t.append(i)
    else:
        for i in range(2,denominator):
            if denominator/i==0 and numerator/i==0:
                t.append(i)
    return t



s=input()
if s[0]!="-":
    s="+"+s
i=1
while i<len(s):
    if s[i]=="-" or s[i]=="+":
        s=s[:i]+" "+s[i:]
        i=i+1
    i=i+1
#print(s)
ls=s.split(" ")
denominator=1#分母
numerator=0#分子
for i in range(len(ls)):
    sign=ls[i][0]
    index=ls[i].index("/")
    x=int(ls[i][1:index])#分子
    y=int(ls[i][index+1:])#分母
    if y!=denominator:
        numerator=numerator*y
        x=x*denominator
        y=y*denominator
        denominator=y
    if sign=="+":
        numerator=numerator+x
    if sign=="-":
        numerator=numerator-x

if numerator%denominator==0:
    result=str(int(numerator/denominator))+"/1"
elif denominator%numerator==0:
    result="1/"+str(int(denominator/numerator))
else:
    t=has()
    while len(t)>0:
        denominator=int(denominator/max(t))
        numerator=int(numerator/max(t))
        t=has()
    result=str(numerator)+"/"+str(denominator)
if result[result.index("/")+1]=="-":
    result="-"+result[:result.index("/")+1]+result[result.index("/")+2]
print(result)





