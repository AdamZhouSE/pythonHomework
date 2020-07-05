def cover(lifeGards,max):
    events = [0 for i in range(max+1)]
    for i in lifeGards:
        for j in range(i[0],i[1]):
            events[j]+=1
    answer=0
    for i in events:
        if i!=0:
            answer+=1
    return answer
times=int(input())
lifeGards=[]
max=0
for i in range(times):
    line=input().split()
    line=[int(x) for x in line]
    if line[1]>max:
        max=line[1]
    lifeGards.append(line)
answerlist=[]
for i in range(times):
    temp=lifeGards.pop(i)
    answerlist.append(cover(lifeGards,max))
    lifeGards.insert(i,temp)
answerlist.sort()
print(answerlist[times-1],end="")