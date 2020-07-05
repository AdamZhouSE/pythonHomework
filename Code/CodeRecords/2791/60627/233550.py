# 16
inp = input()
inp = input()
a = inp.split()
for i in range(len(a)):
    a[i] = int(a[i])
stairs = []
stair = 0
for i,num in enumerate(a):
    if num == i:
        stair += 1
        if i==0:
            continue
        else:
            stairs.append(a[i-1])
stairs.append(a[-1])

print(stair)
outp = ''
for i in stairs:
    outp += i + ' '
print(oupt[:-1])