def diff(a:int,b:int):
    stra = dicts[a]
    strb = dicts[b]
    differ = False
    for ele in range(length):
        if (not differ) and stra[ele]!=strb[ele]:
            differ = True
        elif differ and stra[ele]!=strb[ele]:
            return False
        else:
            continue
    return True

def findconnect(start:int,end:int,path:list):
    path.append(start)
    if start==end:
        paths.append(path)
    if len(path)==length:return
    for ele in conn:
        if ele[0]!=start and ele[1]!=start:
            continue
        else:
            if ele[0]==start:
                if not ele[1] in path:
                    tempath = path.copy()
                    findconnect(ele[1],end,tempath)
            else:
                if not ele[0] in path:
                    tempath = path.copy()
                    findconnect(ele[1],end,tempath)
begin = input()
end = input()
length = len(begin)
dicts = list(eval(input()))
dicts.insert(0,begin)
dicts.append(end)
conn = list()
for i in range(len(dicts)):
    for j in range(i+1,len(dicts)):
        if diff(i,j): conn.append([i,j])
paths = list()
findconnect(0,len(dicts),[])
if len(paths)==0:
    print("[]")
else:
    lengthes = [len(i) for i in paths]
    uses = list(zip(paths,lengthes))
    sortlist = sorted(uses,key=lambda quality:quality[1])
    ans = list()
    for i in range(lengthes.count(min(lengthes))):
        ans.append(sortlist[i][0])
    print(ans)