number=int(input(""))
list=[]
for i in range(number):
    list.append(input("").split(" "))
name=[]
for i in range(number):
    if(not list[i][0] in name):
        name.append(list[i][0])
score=[]
for a in range(len(name)):
    score.append(0)
score_list=[]
for i in range(number):
    score[name.index(list[i][0])]+=int(list[i][1])
    a=[]
    for i in range(len(score)):
        a.append(score[i])
    score_list.append(a)
if(score.count(max(score))==1):
    print(name[score.index(max(score))])
else:
    for i in range(number):
        for a in range(len(name)):
            if(score_list[i][a]>=max(score)):
                print(name[a])
                break
        else:
            continue
        break
                
