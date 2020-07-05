peopleAndHigh=input().split()
people=int(peopleAndHigh[0])
high=int(peopleAndHigh[1])
highetsList=input().split()
highets=[]
for h in highetsList:
    highets.append(int(h))
wide=0
for h in highets:
    if h<=high:
        wide+=1
    else:
        wide+=2
print(wide)