line1=input().split()
n=int(line1[0])
lamps=[[] for i in range(n)]
times=int(line1[1])

for j in range(times):
    line1=input().split()
    line1=[int(x) for x in line1]
    if line1[0]==1:
        for i in range(line1[1]-1,line1[2]):
            lamps[i].append(i)
    else:
        answer=[]
        for i in range(line1[1] - 1, line1[2]):
            if lamps[i].__len__()!=0:
                for j in lamps[i]:
                    answer.append(j)
        answer=list(set(answer))
        if(answer.__len__()==10):
            print(n,times,answer)
        print(answer.__len__())