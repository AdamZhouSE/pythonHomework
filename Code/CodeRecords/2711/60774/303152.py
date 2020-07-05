def isSimilar(s1,s2):
    count = 0
    for i in range(0,len(s1)):
        if(s1[i] != s2[i]):
            count = count + 1
    if(count > 2):
        return False
    else:
        return True

sLst = eval(input())
similar = [[sLst[0]]]
for i in range(1,len(sLst)):
    newStr = sLst[i]
    hasFind = False
    for simi in similar:
        for i in range(0,len(simi)):
            if(isSimilar(newStr,simi[i])):
                simi.append(newStr)
                hasFind = True
                break
        if(hasFind):
            break
    if(not hasFind):
        similar.append(newStr)
print(len(similar))