strs = input()
lists = list()
temp = 0
for i in range(len(strs)):
    if strs[i]=='+' or strs[i]=='-' or i==0:
        for j in range(i+1,len(strs)):
            if strs[j]=='+' or strs[j]=='-' or j==len(strs)-1:
                lists.append(strs[i:j])
                i = j
                break
print(lists)