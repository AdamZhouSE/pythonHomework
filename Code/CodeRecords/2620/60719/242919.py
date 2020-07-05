time = int(input())
total = 0
all = []
for i in range(time):
    total = 0
    inp = int(input())
    for j in range(inp):
        total = total + (j+1) ** 5
    all.append(total)
for i in range(len(all)):
    print(all[i])