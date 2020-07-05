def getEvents(history, l, r):
    result = []
    for end in range(l-1, r):
        result.append(history[:end+1])
    return result

def maxEnd(s1, s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    
    while len(s1) > 0:
        if s2.endswith(s1):
            return len(s1)
        else:
            s1 = s1[1:]
    return 0

def ask(history, sim):
    l, r = list(map(int, input().split()))
    events = getEvents(history, l, r)
    # print(events)
    n = len(events)
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            temp = maxEnd(events[i], events[j])
            if temp > result:
                result = temp
    sim.append(result)

n, m = list(map(int, input().split()))
history = input()
sim = []
for i in range(m):
    ask(history, sim)

for line in sim:
    print(line)