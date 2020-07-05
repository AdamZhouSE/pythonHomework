n=int(input())
light = []
for i in range(n):
    light.append(1)

for i in range(2,n):
    for j in range(i-1,n,i):
        if light[j] == 1:
            light[j] = 0
        else:
            light[j] = 1
if light[n-1] == 1:
    light[n-1] = 0
else:
    light[n-1] = 1
print(light.count(1))

