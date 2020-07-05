line1=input().split()
n=int(line1[0])
lamps=[0 for i in range(n)]
times=int(line1[1])

for i in range(times):
    line1=input().split()
    line1=[int(x) for x in line1]
    if line1[0]==1:
        for i in range(line1[1]-1,line1[2]):
            lamps[i]+=1
    else:
        open=0
        for i in range(line1[1] - 1, line1[2]):
            if lamps[i]>open:
                open=lamps[i]
        print(open)