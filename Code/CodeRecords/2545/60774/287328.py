def addEle(lst,num):
    for i in range(0,len(lst)):
        lst[i].insert(0,num)
    return lst

def generator(lst):
    if(len(lst) == 0):
        return []
    if(len(lst) == 1):
        return[[lst[0]],[]]
    else:
        return generator(lst[1:]) + addEle(generator(lst[1:]),lst[0])

t = int(input())
for i in range(0,t):
    n = int(input())
    numLst = list(map(int,input().split(' ')))
    subSet = list(filter(lambda lst:lst != [],generator(numLst)))
    for sb in subSet:
        if(sum(sb) == 0):
            print('Yes')
            break
    else:
        print('No')