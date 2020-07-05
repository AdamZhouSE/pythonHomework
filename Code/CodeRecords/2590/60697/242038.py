t=int(input())
strs=[]
for i in range(t):
    strs.append(input())
for i in range(t):
    tmp = {}
    for j in range(len(strs[i])):
        if strs[i][j]!="a" and strs[i][j]!="e"  and  strs[i][j]!="i" and  strs[i][j]!="o"  and strs[i][j]!="u":
            if (strs[i][j] in tmp.keys()):
                tmp[strs[i][j]] = tmp[strs[i][j]] + 1
            else:
                tmp[strs[i][j]] = 1
    if(len(tmp)%2==0):
        print("SHE!")
    else:
        print("HE!")