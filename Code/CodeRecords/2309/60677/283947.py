line=input().split()
length=int(line[1])
levels=[]
source=[]
def recursion(source):
    for i in source[:]:
        if i.__len__()==0:
            source.remove(i)
    if source.__len__()==0:
        return 0
    else:
        x=source[0][0]
        for i in source:
            for j in i[:]:
                if j==x:
                    i.remove(j)
        source.pop(0)
        return 1+recursion(source)
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
n=0
for i in range(levels.__len__()):
    for j in range(length):
        if levels[i][j]=="2":
            n+=1
        if levels[i][j]=="1":
            adjacent=[]
            adj=getAdj(levels,length,i,j)
            for k in adj:
                if levels[k[0]][k[1]]=="3":
                    adjacent.append(k[0]*length+k[1])
            source.append(adjacent)
print(recursion(source)+n)