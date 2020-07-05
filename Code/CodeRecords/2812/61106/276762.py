mumber=int(input())
score=input().split()
score.sort()
while(score[0]=='0'):
    score.pop(0)
result=len(score)
for i in range(0,len(score)-1):
    if score[i]==score[i+1]:
        result -= result
print(result)