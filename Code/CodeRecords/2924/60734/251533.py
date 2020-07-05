lst = list(map(int,input().split(' ')))
n, r, avg = int(lst[0]), int(lst[1]), int(lst[2])
data = []
sumScore = 0
for i in range(n):
    data.append(list(map(int,input().split(' '))))
    sumScore+=data[i][0]
extraScore = avg*n-sumScore
data = sorted(data, key = lambda x:x[1])
paper = 0
for i in range(len(data)):
    if extraScore<=0:
        break
    while extraScore>0 and data[i][0]<r:
        paper+=data[i][1]
        extraScore-=1
        data[i][0]+=1
print(paper)