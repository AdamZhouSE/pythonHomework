def whoWin(List):
    scores=[]
    for i in range(len(List[0])):
        scores.append(0)
    for i in range(len(List)):
        for j in range(len(scores)):
            scores[j]+=List[i][j]
    return scores.index(max(scores))+1

nm=list(map(int,input().split(' ')))
List=[]
for i in range(nm[1]):
    lis=list(map(int,input().split(' ')))
    List.append(lis)
print(whoWin(List))