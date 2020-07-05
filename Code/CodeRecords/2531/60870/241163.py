Str = input()
Dict = {}
for ch in Str:
    if ch in Dict.keys():
        Dict[ch] = Dict[ch] + 1
    else:
        Dict[ch] = 1
List = sorted(Dict.items(), key = lambda x:x[1], reverse = True)
resDict = dict(List)
for k in resDict.keys():
    print(k * resDict[k], end = '')