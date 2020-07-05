init=[int(x) for x in input().split()]
numOfStudents=init[0]
students=[]
for i in range(numOfStudents):
    students.append(input())
questions=init[1]
score=[int(x) for x in input().split()]
sum=0
for i in range(questions):
    countA=0
    countB=0
    countC=0
    countD=0
    countE=0
    for j in range(numOfStudents):
        if students[j][i]=='A':
            countA+=1
        elif students[j][i]=='B':
            countB+=1
        elif students[j][i]=='C':
            countC+=1
        elif students[j][i]=='D':
            countD+=1
        elif students[j][i]=='E':
            countE+=1
    sum+=max(countA,countB,countC,countD,countE)*score[i]
print(sum)