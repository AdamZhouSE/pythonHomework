firstLine=input()
n=int(firstLine)
secondLine=input().split()
secondLine.sort(key=int)
waitTime=0
meetPeople=0
for i in secondLine:
    if int(i)>=waitTime:
        meetPeople+=1
        waitTime+=int(i)
print(meetPeople)