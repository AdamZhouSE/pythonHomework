def findLeast(limit,ai):
    loc = 0
    questions = 200001
    for i in range(len(ai)):
        if ai[i]>=limit:
            if ai[i]<questions:
                questions = ai[i]
                loc = i
    if questions == 200001:
        return -1
    else:
        return loc
        
days = int(input())
ai = input().split(" ")
ai = list(map(int,ai))
day = 0
for i in range(days):
    loc = findLeast(i+1,ai)
    if loc == -1:
        break
    day = day + 1
    a = ai.pop(loc)
print(day)
