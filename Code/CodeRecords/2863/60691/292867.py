def position(l, h):
    l.sort()
    for i in range(len(l)):
        if l[i] > h:
            return i

    return len(l)


s1 = input().split(' ')
s2 = input().split(' ')

l1 = []
l2 = []

for i in range(len(s1)):
    l1.append(int(s1[i]))
for i in range(len(s2)):
    l2.append(int(s2[i]))

count = position(l2, l1[1]) + 2*(len(l2) - position(l2, l1[1]))

print(count)

