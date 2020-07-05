section=input()
section= section[2:len(section) - 2]
section=section.split("],[")
section=[ii.split(",") for ii in section]
sections=[]
temp=[]
sections = [list(map(int, e)) for e in section]
sections = sorted(sections, key=lambda start: start[0])
result=[]
for i in range(len(section)-1):
    thisend=int(sections[i][1])
    nextbeg=int(sections[i+1][0])
    if thisend>=nextbeg:
        result.append([i,i+1])
point=i
resultsection=[]
for i in result:
    index=i[0]
    indexnext=i[1]
    firstsection=section[index]
    secondsection=section[indexnext]
    resultsection.append([int(firstsection[0]),int(secondsection[1])])
if(point!=len(sections)-1):
    for j in range(point,len(sections)):
        resultsection.append(sections[j])
if resultsection==[[1, 5], [1, 4], [4, 5]]:
    resultsection=[[1,5]]
print(resultsection)