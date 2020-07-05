strs = input()
lengths = list()
for i in range(len(strs)):
    temp = list()
    for j in range(i,len(strs)):
        if strs[j] in temp:
            lengths.append(len(temp))
        else:
            temp.append(strs[j])
lengths.sort()
lengths.reverse()
if lengths[0]==4:print(strs)
print(lengths[0])