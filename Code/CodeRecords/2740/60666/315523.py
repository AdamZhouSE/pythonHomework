times=eval(input())
times.sort()
times.append(times[0])
result=23*60+59
for i in range(len(times)-1):
    a,b=times[i].split(":")
    c,d=times[i+1].split(":")
    delta=abs((int(c)-int(a))*60+int(d)-int(b))
    if delta>720:
        delta=1440-delta
    result=min(result,delta)
print(result)