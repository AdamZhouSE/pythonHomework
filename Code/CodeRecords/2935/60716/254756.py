strs = input()
index = 0
for i in range(len(strs)):
    if strs[i]=='Q':
        for j in range(i+1,len(strs)):
            if strs[j]=='A':
                for k in range(j+1,len(strs)):
                    if strs[k]=='Q':
                        index+=1
print(index)