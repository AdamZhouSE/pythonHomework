l1 = input().split(',')
s = input()
l2 = s.split(',')

limit = int(l1[len(l1)-1]) - int(l1[0])

for i in range(1, limit):
    l = s.split(',')
    
    for j in range(len(l2)):
        l.append(str(int(l2[j])+i))
        l.append(str(int(l2[j])-i))

    l.sort()

    if l[len(l)-1]>=l1[len(l1)-1] and l[0]<=l1[0]:
        print(i)
        break
