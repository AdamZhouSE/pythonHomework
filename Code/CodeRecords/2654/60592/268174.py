tests = int(input())
rec = []
res = 0
for i in range(0,tests):
    ls = list(map(int,input().split()))
    rec.append(ls)
rec.sort(key = lambda x:x[0])
tem = [0]*rec[tests-1][1]
for i in range(0,tests):
    start = rec[i][0]-1
    end = rec[i][1]-1
    h = rec[i][2]
    for j in range(start,end):
        if tem[j]<h:
            tem[j]=h
print(sum(tem))