strLst = eval(input())
strLst.sort(key = lambda x:len(x))
word = [strLst[0]]
compound = []
for i in range(1,len(strLst)):
    temp = strLst[i]
    for ref in word:
        temp = temp.replace(ref,'')
    if(temp != ''):
        word.append(strLst[i])
        word.sort(key = lambda x:-len(x))
    else:
        compound.append(strLst[i])
compound.sort()
print(compound)