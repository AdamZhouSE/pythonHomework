def seq(l, c):
    for i in range(len(l)):
        if l[i] == c:
            return i


s1 = input()
s2 = input()

l1 = []
for i in range(len(s1)):
    l1.append(s1[i])

lcontain = []
lnot = []
for i in range(len(s2)):
    if s2[i] in l1:
        lcontain.append(s2[i])
    else:
        lnot.append(s2[i])

for i in range(len(lcontain)-1):
    for j in range(i+1,len(lcontain)):
        if seq(s1, lcontain[i]) > seq(s1, lcontain[j]):
            temp = lcontain[i]
            lcontain[i] = lcontain[j]
            lcontain[j] = temp

lresult = lcontain + lnot

print(lresult)