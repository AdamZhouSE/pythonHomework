class player():
    def __init__(self,name,score,time):
        self.name=name
        self.score=score
        self.time=time

def whoWin(List):
    result=[]
    for i in range(len(List)):
        result.append(sum(List[i].score))
    Max=max(result)
    players=[]
    for i in range(len(result)):
        if result[i]==Max:
            players.append(List[i])
    if len(players)==1:
        return players[0].name
    return trueWinner(players,Max)

def trueWinner(List,Max):
    Mintime=100
    name=List[0].name
    Min=List[0]
    for i in range(len(List)):
        need=0
        for j in range(len(List[i].time)):
            need+=List[i].score[j]
            if need>=Max:
                if List[i].time[j]<Mintime:
                    Mintime=List[i].time[j]
                    name=List[i].name
    return name




n = int(input())
List=[]
for i in range(n):
    m=list(map(str,input().split(' ')))
    y=1
    for j in range(len(List)):
        if m[0]==List[j].name:
            List[j].score.append(int(m[1]))
            List[j].time.append(i)
            y=0
            break
    if y==1:
        lis=[]
        lis.append(int(m[1]))
        li=[]
        li.append(i)
        play=player(m[0],lis,li)
        List.append(play)

print(whoWin(List))