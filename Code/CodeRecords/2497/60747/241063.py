target=int(input())
position=input()
position=position[1:len(position)-1].split(",")
s=[]
for i in range(len(position)):
    position[i]=int(position[i])
speed=input()
speed=speed[1:len(speed)-1].split(",")
for i in range(len(speed)):
    speed[i]=int(speed[i])
lst = sorted(zip(position, speed))
times = [(target - p) / s for p, s in lst]
ans = 0

while len(times) > 1:
    lead = times.pop()
    if lead < times[-1]:
        ans += 1
    else:
        times[-1] = lead
print(ans+bool(times))