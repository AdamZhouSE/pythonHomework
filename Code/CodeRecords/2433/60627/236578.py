# 37
from ast import literal_eval
inp = input()
pairs = literal_eval(inp)

useless = []
for i in range(len(pairs)):
    for j in range(len(pairs)):
        if i not in useless and j not in useless:
            if pairs[j][0]<pairs[i][0]<=pairs[j][1] and pairs[j][0]<=pairs[i][1]<pairs[j][1] :
                useless.append(j)
                pairs[i] = pairs[j]
            elif pairs[j][0]<pairs[i][0]<=pairs[j][1] and not pairs[j][0]<=pairs[i][1]<pairs[j][1] :
                useless.append(j)
                pairs[i][0] = pairs[j][0]
            elif not pairs[j][0]<pairs[i][0]<=pairs[j][1] and pairs[j][0]<=pairs[i][1]<pairs[j][1] :
                useless.append(j)
                pairs[i][1] = pairs[j][1]
ans = []
for i in range(len(pairs)):
    if i not in useless:
        ans.append(pairs[i])
print(ans)