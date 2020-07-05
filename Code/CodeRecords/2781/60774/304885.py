import sys
strLst = [[]]
i = 0
while(True):
    line = sys.stdin.readline().strip()
    if line == '':
        break
    if(line == '9'):
        strLst.append([])
        i = i + 1
    else:
        strLst[i].append(line)
for j in range(0,len(strLst)):
    flag = True
    group = strLst[i]
    if(group != []):
        for m in range(0,len(group) - 1):
            print(group[m])
            for n in range(i + 1,len(group)):
                if(group[m] in group[n]):
                    print('Set' + str(i + 1) + 'is not immediately decodable')
                    flag = False
                    break
            if(not flag):
                break
        else:
            print('Set' + str(i + 1) + 'is immediately decodable')