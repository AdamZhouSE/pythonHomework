n=int(input())
marks=[]
for i in range(n):
    mark=input().split(' ')
    mark=list(map(int,mark))
    total=0
    for m in mark:
        total+=m
    marks.append([i+1,total])
marks=sorted(marks,key=lambda x:(-x[1],x[0]))
for i in range(n):
    if marks[i][0]==1:
        print(i+1)
        break