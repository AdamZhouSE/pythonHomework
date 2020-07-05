length=input()
answerList=input().split()
passwordList=input().split()
answer=[]
for i in answerList:
    for n in  passwordList:
        if i == n:
            answer.append(i)
print(' '.join(answer))