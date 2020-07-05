def one_letter_different(x:str,y:str):
    y = list(y)
    for i in range(len(x)):
        if x[i] in y:
            y.remove(x[i])
    return len(y) == 1


def findwords(beginword,words):
    index = 0
    level = [[beginword]]
    q = [beginword]   # q[0]表示前驱 beginword为当前单词
    while q:
        for i in range(len(q)):
            begin = q.pop(0)
            next_level = []
            for x in words[index:]:
                if len(x) == len(begin)+1 and one_letter_different(begin,x):
                    q.append(x)
                    index = words.index(x)
                    for route in level :
                        if route[-1] == begin:
                            next_level.append(route+[x])
                        else:
                            next_level.append(route)
                elif len(x) > len(begin)+1:
                    break
            if len(next_level)>0:
                level = next_level
    return level

words = []
try:
    for line in iter(input,''):
        words.append(line)
except:
    pass

words = sorted(words, key=len)
routes = []
useforstart = [True]*(len(words))
for i in range(len(words)):
    if useforstart[i]:
        valid = findwords(words[i], words[i+1:])
        valid = max(valid,key=len)
        routes.append(valid)
        for x in valid:
            useforstart[words.index(x)] = False
route = max(routes,key=len)
print(len(route))
for x in route:
    print(x)