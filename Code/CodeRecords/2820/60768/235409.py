customers = int(input())
time = []
visit = []
for i in range(customers):
    time.append(input().split(' '))

for e in time:
    if e not in visit:
        visit.append(e)

print(len(time) - len(visit) + 1)