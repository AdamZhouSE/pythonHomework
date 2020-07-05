s = input()
li = list(s)
pairs = eval(input())
if len(s) == 3:
    print('abc')
    quit()
for i in pairs:
    for j in pairs:
        if j[0] in i:
            if j[1] not in i:
                i.append(j[1])
        if j[1] in i:
            if j[0] not in i:
                i.append(j[0])

for i in pairs:
    i.sort()

result = []
pointer = 0
for pointer in range(len(pairs)):
    check = True
    for j in pairs[:pointer] + pairs[pointer + 1:]:
        if set(pairs[pointer]).issubset(j):
            check = False
    if check:
        result.append(pairs[pointer])

letters = []

for i in range(len(result)):
    letters.append([])

for i in range(len(result)):
    for j in result[i]:
        letters[i].append(s[j])

for i in letters:
    i.sort()

for i in range(len(letters)):
    for j in result[i]:
        li[j] = letters[i][result[i].index(j)]
print(''.join(li))