LM = input().split(' ')
L = int(LM[0])
M = int(LM[1])
result = []
for i in range(0,L+1):
    result.append(1)
for a in range(0,M):
    edge = input().split(' ')
    start = int(edge[0])
    end = int(edge[1])
    for i in range(start,end+1):
        result[i] = 0
print(result.count(1))