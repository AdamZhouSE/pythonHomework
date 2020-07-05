number=int(input(""))
list=[]
for i in range(number):
    list.append(input("").split(" "))
name=[]
for i in range(number):
    if(not list[i][0] in name):
        name.append(list[i][0])
score=[0]*len(name)
score_list=[]
for i in range(number):
    score[name.index(list[i][0])]+=int(list[i][1])
    score_list.append(score)
if(score.count(max(score))==1):
    print(name[score.index(max(score))])
