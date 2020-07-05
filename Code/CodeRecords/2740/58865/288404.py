times=eval(input())

def converseToMin(time):
    h=time[:2]
    m=time[-2:]
    total=int(h)*60+int(m)
    return total

times=[converseToMin(i) for i in times]

if 0 in times:
    times.append(24*60)

minGap=24*60
times=sorted(times)

for i in range(len(times)-1):
    temp=times[i+1]-times[i]
    if temp<minGap:
        minGap=temp

print(minGap)
