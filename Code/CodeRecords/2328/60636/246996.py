from itertools import permutations
source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
target=list(permutations(sources,4))
time=[]
for i in target:
    if((i[0]*10+i[1]<=23)&(i[2]*10+i[3]<=59)):
        time.append(i)
time.sort()
if(len(time)!=0):
    print(str(time[-1][0])+str(time[-1][1])+":"+str(time[-1][2])+str(time[-1][3]))
else:
    print("")
    