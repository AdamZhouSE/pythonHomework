def isValid(str1,str2):
    if(len(str1)!=len(str2)):
        print("Length Error")
        return False
    else:
        cnt = 0
        for x in range(len(str1)):
            if(str1[x]!=str2[x]):
                cnt += 1
                if(cnt >= 2):
                    return False
        return True

def find(now,end,path,result):
    if(end in now):
        path.append(end)
        result.append(path)
        return
    else:
        for temp in now:
            tpath = path.copy()
            tpath.append(temp)
            find(graph[temp],end,tpath,result)
        return

start = input()
end = input()
strings = input()[2:-2].split("\",\"")
graph = {}
for string in strings:
    graph[string] = []

for x in range(len(strings)):
    for y in range(x+1,len(strings)):
        if(isValid(strings[x],strings[y])):
            graph[strings[x]].append(strings[y])

minNumber = len(graph)
begin = []
for string in strings:
    if(isValid(string,start)):
        begin.append(string)
res = []
path = [start]
find(begin,end,path,res)

min = len(graph)
result = []
for re in res:
    if(len(re) < min):
        min = len(re)
        result = [re]
    elif(len(re) == min):
        result.append(re)

if(len(result) == 0):
    print("[]")
else:
    out = "[\n"
    outs = []
    for m in result:
        outs.append("[\"" + '\",\"'.join(m) + "\"]")
    out = out + ",\n".join(outs) + "\n]"
    print(out)