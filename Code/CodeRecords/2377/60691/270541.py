s = input()
l = []

for i in range(len(s)):
    if s[i].isdigit():
        l.append(int(s[i]))

print(l)        
if len(l) != 6:
    print(False)
else:
    l1 = [[]for i in range(3)]
    l2 = []

    for i in range(0, 3):
        l1[i].append(l[2*i])
        l1[i].append(l[2*i+1])

    print(l1)

    if l1[0] == l1[1] or l1[1] == l1[2] or l1[0] == l1[2]:
        print(False)
    else:
        for i in range(1, 3):
            l2.append((l1[i][1] - l1[0][1]) / (l1[i][0] - l1[0][0]))
        if l2.count(l2[0]) == 1:
            print(True)
        else:
            print(False)
