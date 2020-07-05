number=input().split(" ")
k=int(number[0])
m=int(number[len(number)-1])
all=[1]
for i in range(1,k+1):
    for j in range(len(all)):
        all.append(all[j]*2+1)
        all.append(all[j]*4+5)
all=list(set(all))
all.sort()
result=""
for i in range(k):
    result+=str(all[i])
print(result)
allnew=[]
for i in range(len(result)):
    allnew.append(result[i])
move=[]
num=0
for i in range(len(allnew)-1):
    if num==m:
        break
    else:
        if allnew[i]<allnew[i+1]:
            move.append(allnew[i])
            num+=1
for i in range(len(move)):
    allnew.remove(move[i])
print(''.join(allnew),end='')