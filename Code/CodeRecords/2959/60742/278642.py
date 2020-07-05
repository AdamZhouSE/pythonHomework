s1 = input()
s2 = input()
l1 = []
l2 = []
res = 0
for i in range(len(s1)):
    for j in range(i,len(s1)):
        l1.append(s1[i:j+1])
for i in range(len(s2)):
    for j in range(i,len(s2)):
        l2.append(s2[i:j+1])
for i in l1:
    for j in l2:
        if i==j:
            res += 1
print(res)