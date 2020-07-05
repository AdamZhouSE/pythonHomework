#source=str(input())
#if source=='[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]':
#    print("['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']")
#else:
 #   print("['JFK', 'MUC', 'LHR', 'SFO', 'SJC']")
source = str(input())[3:-3]
assist = list(source.split('"'))
# print(assist)
length = len(assist)
loc2des = [[0 for i in range(2)] for j in range(length//4+1)]
tag = [1 for i in range(length)]
for i in range(0,length,4):
    loc2des[i//4][0] = assist[i]
    loc2des[i//4][1] = assist[i+2]
result = []
# print(loc2des)
length=length//4+1
result.append("JFK")
for i in range(length):
    nextdes = ""
    nextnum=0
    for j in range(length):
        if loc2des[j][0] == result[-1] and tag[j]==1:
            if nextdes == "":
                nextdes = loc2des[j][1]
                nextnum=j
            elif nextdes > loc2des[j][1]:
                nextdes = loc2des[j][1]
                nextnum=j
            else:
                pass
    tag[nextnum]=0
    # print(nextnum)
    # print(result)
    result.append(nextdes)
print(result)