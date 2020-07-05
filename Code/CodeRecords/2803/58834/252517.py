nm_input = input()
nm = nm_input.split()
n = int(nm[0])
m = int(nm[1])
lights = []
for i in range(1,n+1):
    ai = input()
    ais = ai.split()
    for s in range(1,len(ais)):
        lights.append(int(ais[s]))
lights_new = list(set(lights))
if len(lights_new) == m:
    print("YES")
else:
    print("NO")