s1=input()
s2=input()
res = ""
for i in range(len(s1)):
    if s1[i] in s2:
        tmp = s2.split(s1[i])
        res = res + s1[i] * (len(tmp) - 1)
        s2 = ''.join(tmp)

print(res + s2)
