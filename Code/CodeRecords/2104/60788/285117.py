import sys
people_num=int(input().strip())
person_to_tell=[int(x) for x in input().strip().split()]
info_list=[[i+1] for i in range(people_num)]
game_rounds=[]
for i in range(people_num):
    known=[i+1]
    for k in range(1,people_num+2):
        flag=False
        s=[]
        for ele in known:
            if person_to_tell[ele-1]==i+1:
                game_rounds.append(k)
                flag=True
                break
            else:
                if person_to_tell[ele-1] not in known:
                    s.append(person_to_tell[ele-1])
        known+=s
        if flag:
            break
if len(game_rounds)==0:
    print(-1)
else:
    print(game_rounds)

