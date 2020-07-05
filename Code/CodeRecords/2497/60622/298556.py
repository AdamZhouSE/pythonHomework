target=int(input())
position=eval(input())
speed=eval(input())

cars = sorted(zip(position, speed))
times = [float(target - p) / s for p, s in cars]
ans = 0
while len(times) > 1:
    lead = times.pop()
    if lead < times[-1]:
        ans += 1  
    else:
        times[-1] = lead 

print( ans + bool(times) ) 
