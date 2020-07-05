from itertools import permutations
source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
target=list(permutations([sources],4))
print(target)
time=[]
for i in target:
    if((i[0]*10+i[1]<=24)&(i[2]*10+i[3]<=60)):
        time.append(i)
time.sort()
print(time)
print(str(time[-1][0])+str(time[-1][1])+":"+str(time[-1][2])+str(time[-1][3]))