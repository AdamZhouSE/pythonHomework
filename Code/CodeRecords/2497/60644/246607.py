target=int(input())
position=input()[1:-1].split(',')
speed=input()[1:-1].split(',')
for i in range(0,len(speed)):
    position[i]=int(position[i])
    speed[i]=int(speed[i])
time=[]+position
for i in range(0,len(speed)):
    time[i]=(target-position[i])/speed[i]
for i in range(0,len(time)):
    for j in range(i+1,len(time)):
        if position[i]>=position[j] and time[i]>=time[j]:
            position[j]=position[i]
            time[j]=time[i]
team=0
p=True
for i in range(0,len(speed)):
    for j in range(0,i):
        if time[i]==time[j]:
            p=False
            break
    if p:
        team=team+1
    p=True
print(team)
