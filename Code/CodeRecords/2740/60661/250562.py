time=input()[2:-2].split("\",\"")
rec=[]
for i in range(len(time)):
    temp=int(time[i][:2])*60+int(time[i][3:])
    rec.append(temp)
rec.sort()
mins=24*60
for i in range(1,len(rec)):
    mins=min(rec[i]-rec[i-1],mins)
if rec[0]==0:
    rec[0]=24*60;rec.sort()
    for i in range(1, len(rec)):
        mins = min(rec[i] - rec[i - 1], mins)
print(mins)