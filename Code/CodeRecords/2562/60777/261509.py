n=int(input())
exa=[]
ope=[]
read=[]
unread=[]
trash=[]

for i in range(n):
    tem1=[int(x) for x in input().split()]
    exa.append(tem1)
    tem2=[int(x) for x in input().split()]
    ope.append(tem2)
    
for i in range(n):
    for x in range(1,exa[i][0]+1):
        unread.append(x)
    for j in range(0,2*exa[i][1],2):
        if(ope[i][j]==1):
            read.append(ope[i][j+1])
            unread.remove(ope[i][j+1])
        if(ope[i][j]==2):
            trash.append(ope[i][j+1])
            read.remove(ope[i][j+1])
        if(ope[i][j]==3):
            trash.append(ope[i][j+1])
            unread.remove(ope[i][j+1])
        if(ope[i][j]==4):
            read.append(ope[i][j+1])
            trash.remove(ope[i][j+1])
            
for x in unread:
    print(x,end=' ')
print()
for x in read:
    print(x,end=' ')
print()
for x in trash:
    print(x,end=' ')
print()
    