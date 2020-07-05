n=int(input())
names=[];scores=[]
for i in range(n):
    turn=input().split(' ')
    if names.count(turn[0])==0:
        names.append(turn[0])
        scores.append(int(turn[1]))
    else:
        scores[names.index(turn[0])]+=int(turn[1])
    newIndex=names.index(turn[0])
    if scores[newIndex]>scores[0]:
        temp=scores[0];scores[0]=scores[newIndex];scores[newIndex]=temp
        temp=names[0];names[0]=names[newIndex];names[newIndex]=temp
print(names[0])