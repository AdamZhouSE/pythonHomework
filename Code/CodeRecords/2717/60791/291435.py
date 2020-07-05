l = eval(input())
total = []
res = []
final = True
for i in range(len(l)):
    tem = l[i]
    if tem[0] not in total and tem[3] not in total:
        if(tem[0] == tem[3] and tem[1] == '!'):
            final = False
            break
        elif(tem[0] != tem[3] and tem[1] == '!'):
            total.append(tem[0])
            total.append(tem[3])
            re1 = []
            re1.append(tem[0])
            re2= []
            re2.append(tem[3])
            res.append(re1)
            res.append(re2)
        elif tem[0] != tem[3] :
            re = []
            total.append(tem[0])
            total.append(tem[3])
            re.append(tem[0])
            re.append(tem[3])
            res.append(re)
        else:
            re = []
            total.append(tem[0])
            re.append(tem[0])
            res.append(re)
    elif(tem[0] in total and tem[3] not in total):
        a = tem[0]
        b = tem[3]
        total.append(b)
        if tem[1] == '=':
            for x in range(len(res)):
                if a in res[x]:
                    res[x].append(b)
        else:
            re = []
            re.append(b)
            res.append(res)
    elif(tem[3] in total and tem[0] not in total):
        a = tem[3]
        b = tem[0]
        total.append(b)
        if tem[1] == '=':
            for x in range(len(res)):
                if a in res[x]:
                    res[x].append(b)
        else:
            re = []
            re.append(b)
            res.append(res)
    else:
        a = tem[0]
        b = tem[3]
        
        if tem[1] == '!':
            for x in range(len(res)):
                if a in res[x] and b in res[x]:
                    final = False
                    break
            if(final == False):
                break;
        else:
            for x in range(len(res)):
                if (a in res[x] and b not in res[x]) or(a not in res[x] and b in res[x]):
                    final = False
                    break
            if final == False:
                break
if final:
    print('true')
else:
    print('false')