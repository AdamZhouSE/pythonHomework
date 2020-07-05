import math
def getDir(current,move):
    if(move=='U'):
        return current
    elif(move=='D'):
        if(current=='N'):
            return 'S'
        if(current=='W'):
            return 'E'
        if(current=='E'):
            return 'W'
        if(current=='S'):
            return 'W'
    elif(move=='L'):
        if(current=='N'):
            return 'W'
        if(current=='W'):
            return 'S'
        if(current=='E'):
            return 'N'
        if(current=='S'):
            return 'E'
    elif(move=='R'):
        if(current=='N'):
            return 'E'
        if(current=='W'):
            return 'N'
        if(current=='E'):
            return 'S'
        if(current=='S'):
            return 'W'

def getPla(cp,cd,md,ms):
    ms=int(ms)
    if(md=="U"):
        if(cd=='N'):
            cp[1]+=ms
            return cp
        if(cd=='S'):
            cp[1]-=ms
            return cp
        if(cd=='E'):
            cp[0]+=ms
            return cp
        if(cd=='W'):
            cp[0]-=ms
            return cp
    if(md=="D"):
        if(cd=='N'):
            cp[1]-=ms
            return cp
        if(cd=='S'):
            cp[1]+=ms
            return cp
        if(cd=='E'):
            cp[0]-=ms
            return cp
        if(cd=='W'):
            cp[0]+=ms
            return cp
    if(md=="L"):
        if(cd=='N'):
            cp[0]-=ms
            return cp
        if(cd=='S'):
            cp[0]+=ms
            return cp
        if(cd=='E'):
            cp[1]+=ms
            return cp
        if(cd=='W'):
            cp[1]-=ms
            return cp
    if(md=="R"):
        if(cd=='N'):
            cp[0]+=ms
            return cp
        if(cd=='S'):
            cp[0]-=ms
            return cp
        if(cd=='E'):
            cp[1]-=ms
            return cp
        if(cd=='W'):
            cp[1]+=ms
            return cp

n=int(input())
for i in range(0,n):
    m=input()
    move=input()
    current_dir='N'
    current_pla=[0,0]
    for j in range(0,len(move)-1,4):
        current_pla=getPla(current_pla,current_dir,move[j],move[j+2])
        current_dir=getDir(current_dir,move[j])
    distance=math.sqrt(pow(current_pla[0],2)+pow(current_pla[1],2))
    print(str(int(distance))+" "+current_dir)