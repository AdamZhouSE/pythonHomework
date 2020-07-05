nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
lights = []
for i in range(0, n):
    s = input().split(" ")
    num = int(s[0])
    for j in range(1, num+1):
        lights.append(int(s[j]))
lights = sorted(lights)
length = len(lights)
i = 1
while i < length:
    if lights[i] == lights[i-1]:
        lights.remove(lights[i])
        length -= 1
    else:
        i += 1
if len(lights) == m:
    print("YES")
else:
    print("NO")