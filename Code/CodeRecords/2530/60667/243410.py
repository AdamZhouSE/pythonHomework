s = input()
t = input()
li = []
j=0
for i in s:
    j = t.count(i)
    for x in range(j):
        li.append(i)

for i in t:
    if i not in li:
        li.append(i)

print(''.join(li))