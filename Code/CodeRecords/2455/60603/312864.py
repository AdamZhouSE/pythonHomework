import itertools
def connect(temp:list):
    if len(temp)==1: return True
    tempt = list()
    tempt.append(temp[0][0])
    tempt.append(temp[0][1])
    temp.pop(0)
    while True:
        indext = False
        for el in range(len(temp)):
            if temp[el][0] in tempt and temp[el][1] not in tempt: 
                tempt.append(temp[el][1])
                temp.pop(el)
                indext = True
                break
            if temp[el][1] in tempt and temp[el][0] not in tempt: 
                tempt.append(temp[el][0])
                temp.pop(el)
                indext = True
                break
        if not indext or len(temp)==0:
            break
    if len(temp)>0: 
        return False
    else:
        return True
    
num = int(input())
strs = input().split()
beauty = [int(i) for i in strs]
branch = list()
for i in range(num-1):
    a,b = map(int,input().split())
    branch.append([a,b])
maxs = 0
for i in range(num-1):
    for lists in itertools.combinations(branch,i+1):
        indexs = list()
        for j in lists:
            if j[0] not in indexs:
                indexs.append(j[0])
            if j[1] not in indexs:
                indexs.append(j[1])
        check = connect(list(lists))
        if check:
            index = 0
            for j in indexs:
                index+=beauty[j-1]
            if index>maxs:
                maxs = index
print(maxs,end='')