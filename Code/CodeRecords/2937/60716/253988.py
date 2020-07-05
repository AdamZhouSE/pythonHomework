strs = input()
mode = "CODEFESTIVAL2016"
index=0
for i in range(len(mode)):
    if strs[i]!=mode[i]:
        index+=1
print(index)