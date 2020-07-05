def isSubstring(source,target):
    sp=0
    tp=0
    while(sp<=len(source) and tp<=len(target)):
        if(sp==len(source)-1 and tp<len(target)-1):
            return False
        if(tp>=len(target)):
            return True
        if(target[tp]==source[sp]):
            tp += 1
            sp +=1
        else:
            sp += 1
    return True

source = input()
temp = input()[1:-1].split(",")
dic = []
res = []
for t in temp:
    dic.append(t[1:-1])
for word in dic:
    if(isSubstring(source,word)):
        res.append(word)
longest = max(res,key=len)
print(longest)
