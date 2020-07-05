line1=input().split()
n=int(line1[0])
lamps=[1 for i in range(n)]
times=int(line1[2])

for i in range(times):
    line1=input().split()

    if line1[0]=="C":
        line1[0]=0
        line1=[int(x) for x in line1]
        for j in range(line1[1]-1,line1[2]):
            lamps[j]=line1[3]
    else:
        line1[0]=0
        line1=[int(x) for x in line1]
        answer=[]
        for j in range(line1[1] - 1, line1[2]):
            answer.append(lamps[j])
        answer=list(set(answer))
        print(answer.__len__())