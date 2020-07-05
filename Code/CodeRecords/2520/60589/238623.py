R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
disDic={}
result=[]
for i in range(R):
    for j in range(C):
        dis=abs(i-r0)+abs(j-c0)
        if dis not in disDic:
            disDic[dis]=[]
            disDic[dis].append([i,j])
        else:
            disDic[dis].append([i,j])
for dis in sorted(disDic):
    result.extend(disDic[dis])
print(result)