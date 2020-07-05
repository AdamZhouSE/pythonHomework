line=input().split()
length=int(line[1])
levels=[]
source=[]
bombScale=[]
answers=[]
def recursion(levels,length,answer):
    isAsh=True
    for i in range(levels.__len__()):
        for j in range(length):
            if installBomb([i,j],levels):
                scale=bombScale.copy()
                isAsh=False
                recursion(levels,length,answer+1)
                for axis in scale:
                    x=axis[0]
                    y=axis[1]
                    levels[x][y]=axis[2]
    if isAsh:
        answers.append(answer)
        return

def getAdj(levels,length,i,j):
    answer=[]
    if j!=0:
        if levels[i][j-1]!="#" and levels[i][j-1]!="x" and levels[i][j-1]!="p":
            answer.append([i,j-1])
    if j!=length-1:
        if levels[i][j+1]!="#" and levels[i][j+1]!="x" and levels[i][j+1]!="p":
            answer.append([i,j+1])
    if i!=0:
        if levels[i-1][j]!="#" and levels[i-1][j]!="x" and levels[i-1][j]!="p":
            answer.append([i-1,j])
    if i!=levels.__len__()-1:
        if levels[i+1][j]!="#" and levels[i+1][j]!="x" and levels[i+1][j]!="p":
            answer.append([i+1,j])
    return answer
def installBomb(axis,levels):
    bombScale.clear()
    x=axis[0]
    y=axis[1]
    if levels[x][y]=="*":
        for i in range(0,x):
            if levels[x-1-i][y]=="#":
                break
            else:
                bombScale.append([x-1-i,y,levels[x-1-i][y]])
                levels[x-1-i][y]="p"
        for i in range(x,levels.__len__()):
            if levels[i][y]=="#":
                break
            else:
                bombScale.append([i,y,levels[i][y]])
                levels[i][y]="p"
        for i in range(0,y):
            if levels[x][y-1-i]=="#":
                break
            else:
                bombScale.append([x,y-1-i,levels[x][y-1-i]])
                levels[x][y-1-i]="p"
        for i in range(y+1,length):
            if levels[x][i]=="#":
                break
            else:
                bombScale.append([x,i,levels[x][i]])
                levels[x][i]="p"
        return True
    else:
        return False
for i in range(int(line[0])):
    line=list(input())
    levels.append(line)
answer=0
recursion(levels,length,answer)
answers.sort(reverse=True)
print(answers[0])