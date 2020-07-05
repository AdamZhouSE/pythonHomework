str = input()
indexlist = list(eval(input()))
notes = []
#notes for pairs which can change with each other
lists = []
#lists for noting which has emerged
for i in range(len(indexlist)):
    if not (indexlist[i][0] in lists or indexlist[i][1] in lists):
        notes.append(indexlist[i])
        lists.append(indexlist[i][0])
        lists.append(indexlist[i][1])
#        print("{} and {}".format(indexlist[i][0],indexlist[i][1]))
    else:
        for k in range(len(notes)):
            templist = list(notes[k])
            for j in range(len(templist)):
                if templist[j]==indexlist[i][0] :
                    templist.append(indexlist[i][1])
                    lists.append(indexlist[i][1])
                elif templist[j]==indexlist[i][1]:
                    templist.append(indexlist[i][0])
                    lists.append(indexlist[i][0])
            notes[k] = templist
strs = list(str)
for i in range(len(notes)):
    index = list(notes[i])
    letters = list()
    for j in range(len(index)):
        letters.append(strs[index[j]])
    letters.sort()
    index.sort()
    for j in range(len(index)):
        strs[index[j]]=letters[j]
strss = ''.join(strs)
print(strss)