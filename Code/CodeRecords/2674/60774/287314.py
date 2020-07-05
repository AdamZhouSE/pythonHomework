def preCode(s):
    s = s[s.find('a'):]  
    if(s[len(s) - 1] != 'c'):
        s = s[:s.rfind('c') + 1]
    return s

def addEle(lst,ind):
    for i in range(0,len(lst)):
        lst[i].insert(0,ind)
    return lst

def generator(indexLst):
    if(len(indexLst) == 0):
        return []
    if(len(indexLst) == 1):
        return[[indexLst[0]],[]]
    else:
        return generator(indexLst[1:]) + addEle(generator(indexLst[1:]),indexLst[0])
    
def locateB(s):
    indexLst = []
    for i in range(0,len(s)):
        if(s[i] == 'b'):
            indexLst.append(i)
    return indexLst

t = int(input())
for i in range(0,t):
    count = 0
    s = preCode(input())
    permutation = list(filter(lambda lst:lst != [],generator(locateB(s))))
    for perm in permutation:
        if(len(perm) == 1):
            numOfA = s[:perm[0]].count('a')
            numOfC = s[perm[0] + 1:].count('c')
        else:
            numOfA = s[:perm[0]].count('a')
            numOfC = s[perm[-1] + 1:].count('c')
        count = count + (int(pow(2,numOfA)) - 1) * (int(pow(2,numOfC)) - 1)
    print(count)