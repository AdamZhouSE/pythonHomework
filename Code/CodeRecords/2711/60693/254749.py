def is_similar(s1,s2):
    same_ch=0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            same_ch += 1
    if same_ch == len(s1) or same_ch == len(s1)-2:
        return True
    else:
        return False

strs=eval(input())
res=[]
res.append([strs[0]])
for i in range(1,len(strs)):
    match = False
    for group in res:
        for s in group:
            if is_similar(s,strs[i]):
                group.append(strs[i])
                match = True
                break
    if not match:
        res.append([strs[i]])

print(len(res))