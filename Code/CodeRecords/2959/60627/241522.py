# 15
s1 = input()
s2 = input()
t = 0
for i in range(len(s1)):
    for j in range(i,len(s1)+1):
        sub = s2[:]
        while sub.find(s1[i:j]) != -1 and len(s1[i:j])!= 0:
            ind = sub.find(s1[i:j])
            sub = sub[:ind]  + sub[ind + j -i:]
            t += 1
print(t)    
            