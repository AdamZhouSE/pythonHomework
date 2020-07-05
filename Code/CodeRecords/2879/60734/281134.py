n = int(input())
crossings=[]
for i in range(n**2):
    crossings.append(list(map(int,input().split(' '))))

row = [i for i in range(1,n+1)]
col = [i for i in range(1,n+1)]
work = []
for i in range(len(crossings)):
    if crossings[i][0] in row \
    and crossings[i][1] in col:
        row.remove(crossings[i][0])
        col.remove(crossings[i][1])
        work.append(i+1)
work = list(map(str,work))
print(' '.join(work))