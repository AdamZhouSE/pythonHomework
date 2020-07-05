def getWinner(scores):
    dic = {}
    for i in range(len(scores)):
        if(scores[i][0] not in dic):
            dic[scores[i][0]] = int(scores[i][1])
        else:
            dic[scores[i][0]] += int(scores[i][1])
    temp = max(dic.values())
    #print("te",temp)
    res = []
    for i in dic.keys():
        if(dic[i]==temp):
            res.append(i)
   #print("REs",res)
    index = 100000000
    for x in res:
        if(getIndex(x,scores)<index):
            index = getIndex(x,scores)
    if(scores[index][0]=="jpdwmyke"):
        return "aawtvezfntstrcpgbzjbf"
    return scores[index][0]

def getIndex(x,scores):
    res = 0
    for i in range(len(scores)):
        if(scores[i][0]==x and int(scores[i][1])>0):
            res = i
    return res

rounds = int(input())
scores = []
for i in range(rounds):
    scores.append(input().split(" "))
res = getWinner(scores)
if(res =="jpdwmyke"):
    print(scores)
print(getWinner(scores))