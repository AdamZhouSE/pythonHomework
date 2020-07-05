# 15
s1 = input()
s2 = input()
t = 0
for i in range(len(s1)):
    for j in range(i,len(s1)):
        sub = s2[:]
        while sub.find(s1[i:j]) != -1:
            sub = sub[:i]  + sub[j:]
            t += 1
print(t)    
            