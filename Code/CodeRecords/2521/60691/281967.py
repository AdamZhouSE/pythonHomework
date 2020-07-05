import itertools


def isunequal(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False

    return True


s = input()
s = s.strip('[]')
l = s.split(',')

l2 = []
for i in range(len(l)):
    l2.append(int(l[i]))

l1 = list(itertools.permutations(l2))

for i in range(len(l1)):
    if isunequal(list(l1[i])):
        print(list(l1[i]))
        break