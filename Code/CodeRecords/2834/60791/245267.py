n,m = [int(i) for i in input().split()]
x = 0
answers = []
while(x <n):
    answers.append(input())
    x+=1
score = [int(i) for i in input().split()]
total = 0
for i in range(m):
    an_num = [0,0,0,0,0]
    for k in range(n):
        if(answers[k][i]=='A'):
            an_num[0]+=1
        elif(answers[k][i]=='B'):
            an_num[1]+=1
        elif(answers[k][i]=='C'):
            an_num[2]+=1    
        elif(answers[k][i]=='D'):
            an_num[3]+=1    
        elif(answers[k][i]=='E'):
            an_num[4]+=1
    total += score[i]*max(an_num)
print(total)