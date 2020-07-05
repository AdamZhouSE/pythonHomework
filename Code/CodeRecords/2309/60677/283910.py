line=input().split()
length=int(line[1])
levels=[]
source=set()
n=0
def getAdj(levels,length,i,j):
    answer=[]
    if j!=0:
        answer.append([i,j-1])
    if j!=length-1:
        answer.append([i,j+1])
    if i!=0:
        answer.append([i-1,j])
    if i!=levels.__len__()-1:
        answer.append([i+1,j])
    return answer
for i in range(int(line[0])):
    line=list(input())
    levels.append(line)
for i in range(levels.__len__()):
    for j in range(length):
        if levels[i][j]=="2":
            n+=1
        if levels[i][j]=="1":
            adj=getAdj(levels,length,i,j)
            for k in adj:
                if levels[k[0]][k[1]]=="3":
                    source.add(k[0]*length+k[1])
print(n+source.__len__())