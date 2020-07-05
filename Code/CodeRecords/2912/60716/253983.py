strs = input()
lengths = list()
for i in range(len(strs)):
    print("{}:".format(i))
    temp = list()
    for j in range(i,len(strs)):
        if strs[j] in temp:
            lengths.append(len(temp))
            print(temp)
        else:
            temp.append(strs[j])
lengths.sort()
lengths.reverse()
print(lengths[0])