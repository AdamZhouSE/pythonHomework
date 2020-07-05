import copy

s = list(input())
t = list(input())

l = ['']*len(s)

for i in range(len(t)):
    f = False
    for j in range(len(s)):
        if t[i]==s[j]:
            l[j]=l[j]+s[j]
            f = True
            break
    if f ==False:
        l.append(t[i])
print("".join(l))
