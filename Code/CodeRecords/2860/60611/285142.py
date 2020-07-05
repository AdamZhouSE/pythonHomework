number=int(input())
l=[]
for i in range(number):
    l.append(list(map(int,input().split(" "))))
tag=0
assist=[-1 for i in range(number)]

def findabletoreach(t,n):
    for i in range(number):
        if l[n][0]==l[i][0] or l[n][1]==l[i][1]:
            if assist[i]==-1:
                assist[i]=t
                findabletoreach(t,i)

while -1 in assist:
    tag+=1
    position=assist.index(-1)
    findabletoreach(tag,position)
s=set(assist)
print(len(s)-1)