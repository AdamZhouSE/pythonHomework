def mingap(a,b):
    hour1=int(a[0:2])
    hour2=int(b[0:2])
    m1=int(a[3:])
    m2=int(b[3:])
    
    x=hour1-hour2
    y=m1-m2
    if x<0 :
        x=24-abs(x)
    if y<0:
        y=60+y
        x-=1
    time1=x*60+y
    
    x=hour2-hour1
    y=m2-m1
    if x<0 :
        x=24-abs(x)
    if y<0:
        y=60+y
        x-=1
    time2=x*60+y
    
    return min(time1,time2)
        
get=eval(input())
out=[]
for i in range(len(get)):
    for j in range(i+1,len(get)):
        out.append(mingap(get[i],get[j]))
print(min(out))
        