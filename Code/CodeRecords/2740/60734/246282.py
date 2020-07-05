def minus(a,b):
    if a[0] >= b[0]:
        time = (a[0]-b[0])*60+a[1]-b[1]
    else:
        time = (b[0]-a[0])*60+b[1]-a[1]
    if time>12*60:
        return 24*60-time
    else:
        return time
import re
lst = re.findall(r'"(.*?)"',input())
for i in range(len(lst)):
    hour = int(lst[i][:2])
    minute = int(lst[i][3:])
    lst[i] = [hour,minute]
min_time = 24*60
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        time = minus(lst[i],lst[j])
        if time <min_time:
            min_time = time
print(min_time)