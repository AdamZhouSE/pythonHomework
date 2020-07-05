def copyAndpaste(source,target):
    sdic ={}
    tdic ={}
    for t in target:
        if(t not in tdic.keys()):
            tdic[t] = 1
        else:
            tdic[t] += 1
    for s in source:
        if(s not in sdic.keys()):
            sdic[s] = 1
        else:
            sdic[s] += 1
    keys = dict.keys(tdic)
    for key in keys:
        if(key not in sdic):
            return "NO"
        elif(tdic[key]>sdic[key]):
            return "NO"
    return "YES"

source = input().replace(" ","")
target = input().replace(" ","")
print(copyAndpaste(source,target)，end = "")