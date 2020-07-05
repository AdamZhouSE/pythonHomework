students_questions=list(map(int,input().split()))
answers = [[]*students_questions[1]]*students_questions[0]
for i in range(students_questions[0]):
    answers[i]=list(input())
score = list(map(int,input().split()))
result=0
for i in range(students_questions[1]):
    temp = [0] * 5
    for j in range(students_questions[0]):
        if answers[j][i]=="A":
            temp[0]+=1
        elif answers[j][i]=="B":
            temp[1]+=1
        elif answers[j][i]=="C":
            temp[2]+=1
        elif answers[j][i]=="D":
            temp[3]+=1
        else :
            temp[4]+=1

    result=max(temp)*score[i]+result
print(result)

