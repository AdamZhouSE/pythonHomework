
target=int(input())
inp=input()
position=inp[1:-1].split(",")
for i in range(len(position)):
    position[i]=int(position[i])
inp=input()
speed=inp[1:-1].split(",")
for i in range(len(speed)):
    speed[i]=int(speed[i])
if len(position) == 1 or not position:
    print (len(position))
else:
    times = [(target-pos)/spe for pos, spe in zip(position, speed)]
    res = [(i, j) for i, j in zip(position, times)]
    res.sort(key=lambda x:x[0])
    count = 1
    big = res[-1][1]
    for i in range(len(res)-2,-1,-1):
        if res[i][1] > big:
            big = res[i][1]
            count += 1
            continue
    print (count)

