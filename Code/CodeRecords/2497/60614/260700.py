target=int(input())
position=eval(input())
speed=eval(input())
cars=sorted(zip(position,speed),reverse=True)
time=[]
for i in cars:
    time.append((target-i[0])/i[1])
i=len(time)-1
while i>0:
    if time[i]<=time[i-1]:
        del time[i]
    i-=1
print(len(time))