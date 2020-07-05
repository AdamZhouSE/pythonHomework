# 15
inp = input()
inp = input()
a = inp.split()
for i in range(len(a)):
    a[i] = int(a[i])
inp = input()
b = inp.split()
for i in range(len(b)):
    b[i] = int(b[i])
    
a.sort()
l = []
for i in b:
    if i >= a[-1]:
        l.append(len(a))
        continue
    for j in range(len(a)):
        if a[j]>i:
            l.append(j)
            break
outp = ''
for i in l:
    outp += str(i) + ' '
print(outp[:-1])