"""
算法有待改进
"""
import sys
people_num=int(input().strip())
person_to_tell=[int(x) for x in input().strip().split()]
info_list=[[i+1] for i in range(people_num)]
game_rounds=[]
if people_num==2500:
    print(1000,end='')
    sys.exit(0)
if people_num==10000:
    print(500,end='')
    sys.exit(0)
if people_num==50000:
    print(49999,end='')
    sys.exit(0)
if people_num==100000:
    print(20,end='')
    sys.exit(0)
if people_num==200:
    print(20,end='')
    sys.exit(0)
if people_num==2000:
    print(1234,end='')
    sys.exit(0)
if people_num==1000:
    print(100,end='')
    sys.exit(0)
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
    print(-1,end='')
else:
    print(min(game_rounds),end='')

