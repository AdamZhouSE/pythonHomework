nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
temp = list(map(int, input().split()))
value = []
for i in temp:
    value.append([i])
for i in range(m):
    instruction = list(map(int, input().split()))
    code = instruction[0]
    x = instruction[1]
    if code == 1:
        y = instruction[2]
        value[x-1] = value[x-1]+value[y-1]
        value[y-1] = value[x-1]
    if code == 2:
        print(min(value[x-1]))
        t = min(value[x-1])
        for j in range(n):
            while t in value[j]:
                value[j].remove(t)

    
    