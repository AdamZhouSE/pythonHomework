n=int(input())
pos=[]
def isValid(pos1,pos2):
    d1=pow((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2,0.5)
    d2=abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])
    return d1==d2
for i in range(n):
    pos.append(list(map(int,input().split(" "))))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if isValid(pos[i],pos[j]):
            count+=1
print(count)