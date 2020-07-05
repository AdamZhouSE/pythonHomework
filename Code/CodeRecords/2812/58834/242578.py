#输入n和成绩，并把成绩分隔放入列表
n=input()
scores=input()
scores_split=scores.split(' ')
new_scores=[]
#双循环把不重复的数字放在一个列表中
for number in range(0,len(scores_split)):
    state=True
    for m in range(number+1,len(scores_split)):
        if scores_split[number]==scores_split[m]:
            state=False
            break
        else:
            continue
    if state:
        new_scores.append(scores_split[number])
#判断有无0
lenth = len(new_scores)

for s in range(0,len(new_scores)):
    if new_scores[s]=='0':
        lenth = len(new_scores)-1



print(lenth)
