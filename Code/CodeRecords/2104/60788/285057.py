import sys
people_num=int(input().strip())
person_to_tell=[int(x) for x in input().strip().split()]
info_list=[[i+1] for i in range(people_num)]
game_round=1
while True:
    for i in range(people_num):
        update_message=info_list[i]
        update_loc=person_to_tell[i]-1
        if update_loc+1 in update_message:
            print(game_round)
            sys.exit(0)
        else:
            for k in update_message:
                if k not in info_list[update_loc]:
                    info_list[update_loc].append(k)
            
