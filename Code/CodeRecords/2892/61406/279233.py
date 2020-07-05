source=input().split(' ')
M = int(source[0])
N = int(source[1])
statistics = []
for i in range(0,10):
    statistics.append(0)
for num in range(M,N+1):
    for x in str(num):
        statistics[int(x)]+=1
if M==0:
    statistics[0]-=1
for j in range(0,9):
    print(statistics[j],end=' ')
print(statistics[9],end='')
