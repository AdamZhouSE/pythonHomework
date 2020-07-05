line1=input().split()
n=int(line1[0])
lamps=[[] for i in range(n)]
times=int(line1[1])

for i in range(times):
    line1=input().split()
    line1=[int(x) for x in line1]
    if line1[0]==1:
        for j in range(line1[1]-1,line1[2]):
            lamps[j].append(i)
    else:
        answer=[]
        for j in range(line1[1] - 1, line1[2]):
            if lamps[j].__len__()!=0:
                for k in lamps[j]:
                    answer.append(k)
        answer=list(set(answer))
        print(answer.__len__())