first=input().split(' ')
numSubjects=int(first[0])
eachTime=int(first[1])
chapters=input().split(' ')
chapters=list(map(int,chapters))
chapters.sort()
totalTime=0
for chapter in chapters:
    totalTime+=eachTime*chapter
    if eachTime>1:
        eachTime=eachTime-1
print(totalTime)