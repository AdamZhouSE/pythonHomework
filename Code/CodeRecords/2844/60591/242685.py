t = int(input().split(" ")[1])
time = list(map(int,input().split(" ")))

max = 0
n = 0
for x in range(len(time)):
    n = 0
    free = t
    for y in range(x,len(time)):
        if(free >= time[y]):
            n += 1
            free -= time[y]
        else:
            if(max < n):
                max = n
            n = 0
            break
    if(n != 0 and max < n):
        max = n
print(max)