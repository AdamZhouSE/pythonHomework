target = eval(input())
position = list(map(int,input()[1:-1].split(",")))
speed = list(map(int,input()[1:-1].split(",")))

dict = {}
for x in range(len(position)):
    dict[position[x]] = speed[x]
position.sort(reverse = True)

time = []
for m in position:
    length = target - m
    time.append(length/dict[m])
now = time[0]
count = 0
for x in range(1,len(time)):
    if(time[x] > now):
        count += 1
        now = time[x]
    else:
        continue
count += 1
print(count)