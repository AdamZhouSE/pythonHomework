rounds = eval(input())
name = []
score = []
ns = []
for i in range(0,rounds):
    ns.append(input().split())
    if ns[i][0] in name:
        index = name.index(ns[i][0])
        score[index] = score[index]+int(ns[i][1])
    else:
        name.append(ns[i][0])
        score.append(int(ns[i][1]))
mscore = max(score)
cnt = 1
winner = []
for i in range(0,len(score)):
    if score[i]==mscore:
        cnt+=1
        winner.append(name[i])
if cnt==1:
    print(name[score.index(mscore)])
else:
    name0 = []
    score0 = []
    for i in range(0,len(ns)):
        if ns[i][0] in winner:
            if ns[i][0] in name0:
                index = name0.index(ns[i][0])
                score0[index] = score0[index]+int(ns[i][1])
                if score0[index]>=mscore:
                    print(name0[index])
                    break
            else:
                name0.append(ns[i][0])
                score0.append(int(ns[i][1]))
                if int(ns[i][1])>=mscore:
                    print(ns[i][0])
                    break