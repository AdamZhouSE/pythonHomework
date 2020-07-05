l1 = input().split(',')
l2 = input().split(',')
teststr = ''.join(l1)

limit = int(l1[len(l1)-1]) - int(l1[0])

for i in range(1, limit):
    l = l2
    for j in range(len(l2)):
        l.append(str(int(l2[j])+i))
        l.append(str(int(l2[j])-i))

    l.sort()
    s = ''.join(l)
    if teststr in s:
        print(i)
        break