line1=input().split()
n=int(line1[0])
lamps=[0 for i in range(n)]
times=int(line1[1])

for i in range(times):
    line1=input().split()
    line1=[int(x) for x in line1]
    if line1[0]==0:
        for i in range(line1[1]-1,line1[2]):
            lamps[i]=(lamps[i]+1)%2
    else:
        open=0
        for i in range(line1[1] - 1, line1[2]):
            if lamps[i]==1:
                open+=1
        print(open)