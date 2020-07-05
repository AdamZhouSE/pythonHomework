target = int(input())
position = eval(input())
speed = eval(input())
time = []
for i in range(len(position)):
    time.append((target - int(position[i]))/int(speed[i]))
teamNum = len(position)
for i in range(len(position)):
    for j in range(i+1, len(position)):
        if time[i] == time[j]:
            teamNum = teamNum - 1
        elif time[i] > time[j] and position[i] > position[j]:
            teamNum = teamNum - 1
        elif time[i] < time[j] and position[i] < position[j]:
            teamNum = teamNum - 1
print(teamNum)