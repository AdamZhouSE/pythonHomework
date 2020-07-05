tem = input()[1:-1].split(',')
start = []
effect = []
for n in tem:
    start.append(int(n))
tem = input()[1:-1].split(',')
end = []
cnt = 0
for n in tem:
    end.append(int(n))
    effect.append(int(n) - start[cnt])
    cnt = cnt + 1
tem = input()[1:-1].split(',')
profit = []
cnt = 0
for n in tem:
    profit.append(int(n))
    effect[cnt] = int(n) / effect[cnt]
    cnt = cnt + 1

result = 0
time = [10000,0]
while len(effect) != 0:
    index = effect.index(max(effect))
    if end[index] <= time[0]:
        result = result + profit[index]
        time[0] = start[index]
    elif start[index] >= time[1]:
        result = result + profit[index]
        time[1] = end[index]
    del start[index]
    del end[index]
    del profit[index]
    del effect[index]
print(result)