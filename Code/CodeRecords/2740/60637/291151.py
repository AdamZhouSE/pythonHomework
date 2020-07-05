times=eval(input())
record=float('Inf')
for i in range(len(times)):
    for j in range(i+1,len(times)):
        temp=(int)(times[i][0:2])-(int)(times[j][0:2])
        if(temp>0):
            time=temp*60+(int)(times[i][3:5])-(int)(times[j][3:5])
        else:
            time=-temp*60-(int)(times[i][3:5])+(int)(times[j][3:5])
        time=1440-time if 1440-time<time else time
        if(time<record):
            record=time
print(record)
