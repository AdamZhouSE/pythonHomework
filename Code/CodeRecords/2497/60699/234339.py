target=int(input())
position=input()
speed=input()
position=position[1:(len(position)-1)]
position=list(map(int,position.split(',')))
speed=speed[1:(len(speed)-1)]
speed=list(map(int,speed.split(',')))
cars = sorted(zip(position, speed))
times = [float(target - p) / s for p, s in cars]
ans = 0
while len(times) > 1:
    lead = times.pop()
    if lead < times[-1]: ans += 1 
    else: times[-1] = lead

print(ans + bool(times)) 