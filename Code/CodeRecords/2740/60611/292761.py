time=eval(input())
times=[]
for i in time:
    a=60*int(i[0:2])+int(i[3:5])
    times.append(a)
times=sorted(times)
sub=[]
for i in range(1,len(times)):
    sub.append(times[i]-times[i-1])
sub.append(times[0]-times[-1]+24*60)
print(min(sub))