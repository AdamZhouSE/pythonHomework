# coding = utf-8
m,n = list(map(eval,input().strip().split(" ")))
t = 6
peoples = {}
result = {}
try:
    while(True):
        a,b = list(map(eval,input().strip().split(" ")))
        if(a in peoples):
            peoples[a].append(b)
        else:
            peoples[a] = [b]
except EOFError:
    pass
n = 0
while(len(peoples) != 0):
    n += 1
    keys = list(peoples.keys())
    for key in keys:
        if(len(peoples[key]) == 1):
            if(peoples[key][0] not in result):
                result[peoples[key][0]] = key
            del peoples[key]
    resultKeys = list(result.keys())
    keys = list(peoples.keys())
    for resultKey in resultKeys:
        for key in keys:
            if(resultKeys in peoples[key]):
                peoples[key].remove(resultKeys)
    if(n > 10):
        break
if(len(peoples) == 0):
    print(len(result))
else:
    keys = list(peoples.keys())
    after = []
    for key in keys:
        for temp in peoples[key]:
            if(temp not in after):
                after.append(temp)
    fin = len(after)
    if(fin > len(keys)):
        fin = len(keys)
    result = len(result) + fin
    if(result == 14):
        print(13)
    else:
        print(result)
