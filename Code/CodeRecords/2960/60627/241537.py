# 16
input()
s1 = input()
s2 = input()
t = 0
for i in range(len(s2)):
    ok = True
    for j in raneg(len(s1)):
        if s2[i + j] != s1[j] and s2[i + j] !='*' and  s1[j]!='*':
            ok = False
    if ok:
        t +=1
        
print(y)