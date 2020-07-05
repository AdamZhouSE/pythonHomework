l=[]
l.append(input())
l.append(input())
request=list(map(int,l[0].split()))
people=list(map(int,l[1].split()))
peopleNumber=request[0]
restrict=request[1]
number=0
for i in range(peopleNumber):
    for j in range(i+1,peopleNumber):
        if abs(people[i]-people[j])<=restrict:
            number+=1
number*=2
print(number)