def is_intersect(w1,w2):
    for i in range(len(w1)):
        for j in range(len(w2)):
            if w1[i] == w2[j]:
                return True
    return False

strs=eval(input())
maxlen=0
for i in range(len(strs)-2):
    for j in range(i+1,len(strs)):
        if not is_intersect(strs[i],strs[j]):
            tmplen=len(strs[i])*len(strs[j])
            maxlen=max(maxlen,tmplen)
if not is_intersect(strs[-2],strs[-1]):
    tmplen=len(strs[-2])*len(strs[-1])
    maxlen=max(maxlen,tmplen)

print(maxlen)