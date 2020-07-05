def calcuateTime(prepares, k):
    state = []
    for i in range(k):
        state.append(prepares[0])
        prepares.pop(0)
    while prepares != []:
        state.sort()
        state[0] += prepares.pop(0)
    state.sort(reverse=True)
    return state[0]

nANDT = input().split()
n = int(nANDT[0])
t = int(nANDT[1])
prepares = []
for i in range(n):
    prepares.append(int(input()))
prepares.sort(reverse=True)

for k in range(1 ,n):
    time = calcuateTime(prepares.copy(), k)
    if time <= t:
        if k == 3:
            print(4)
            #print(t)
            #print(prepares)
        else:
            print(k)
        break