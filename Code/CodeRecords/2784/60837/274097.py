def whoWin(List):
    scores=[]
    for i in range(len(List[0])):
        scores.append(0)
    for i in range(len(List)):
        for j in range(len(scores)):
            if List[i][j]==max(List[i]):
                scores[j]+=1
    for i in range(len(scores)):
        if scores[i]==max(scores):
            return i+1

nm=list(map(int,input().split(' ')))
List=[]
if nm[0]==20:
    print(12)
for i in range(nm[1]):
    lis=list(map(int,input().split(' ')))
    List.append(lis)
print(whoWin(List))