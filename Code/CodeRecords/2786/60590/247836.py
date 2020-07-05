games = int(input())
ques = list(map(int, input().split()))
ques.sort()
#print(ques)

train = 0
for i in range(games):
    quesPerday = i+1
    if quesPerday > ques[i]:
        continue
    else:
        train = train+1
print(train)