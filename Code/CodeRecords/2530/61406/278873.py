s = input()
T = input()
sequence = []
statistics = []
for i in range(0,26):
    sequence.append(0)
    statistics.append(0)
t=1
for i in s:
    sequence[ord(i)-ord('a')]=t
    t+=1
for x in T:
    statistics[ord(x)-ord('a')]+=1
kind=0
for x in statistics:
    if x!=0:
        kind+=1
result=""
for j in range(1,max(sequence)+1):
    index = sequence.index(j)
    for k in range(0,statistics[index]):
        result = result+chr(ord('a')+index)
    statistics[index]=0
for x in range(0, 26):
    if statistics[x] != 0:
        index = x
    for k in range(0,statistics[index]):
        result = result+chr(ord('a')+index)
    statistics[index]=0
print(result)

