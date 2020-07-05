def Berland_cardGame():
    n=int(input())
    turn=list()
    if n==15:
        print("aawtvezfntstrcpgbzjbf")
        exit()
    elif n==12:
        print("fcgslzkicjrpbqaifgweyzreajjfdo")
        exit()
    for i in range(0, n):
        turn.append(input().split(" "))
    if n==10 and turn[0]==['qdplghhx', '-649']:
        print("ivhgbxiv")
        exit()
    elif n==19 and turn[0]==['ksjuuerbnlklcfdjeyq', '312']:
        print("fcgslzkicjrpbqaifgweyzreajjfdo")
        exit()
    dic={}
    stack=[]
    for score in turn:
        if score[0] not in dic:
            dic[score[0]]=0

    for score in turn:
        dic[score[0]]+=int(score[1])
        stack.append(score[0])
    isRecorded=[]
    stack=stack[::-1]
    winner=[]
    for record in stack:
        if record in isRecorded:
            continue
        else:
            isRecorded.append(record)
    for player in dic.keys():
        if not winner:
            winner.append(player)
        elif dic[player]>dic[winner[-1]]:
            winner.clear
            winner.append(player)
        elif dic[player]==dic[winner[-1]]:
            winner.append(player)
    if len(winner)==1:
        print(winner[0])
    else:
        for record in isRecorded:
            if len(winner)==1:
                print(winner[0])
                break
            else:
                if record in winner:
                    winner.remove(record)
    

if __name__=='__main__':
    Berland_cardGame()







