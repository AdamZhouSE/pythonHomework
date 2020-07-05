import itertools
import math


def isrectangle(l):
    if l[0][0] ==l[1][0] or l[2][0] == l[3][0] or l[0][0] == l[2][0] or l[1][0] == l[3][0]:
        if (int(l[0][1]) - int(l[2][1])) / (int(l[0][0]) - int(l[2][0])) == (int(l[1][1]) - int(l[3][1])) / (int(l[1][0]) - int(l[3][0])) and l[0] != l[1]:
            return True
    else:
        if (int(l[0][1]) - int(l[1][1])) / (int(l[0][0]) - int(l[1][0])) == (int(l[2][1]) - int(l[3][1])) / (int(l[2][0]) - int(l[3][0])) and l[0] != l[2]:
            return True
    return False


def areacalculate(l):
    return distancecalculate(l[0], l[1]) * distancecalculate(l[0], l[2])


def distancecalculate(l1, l2):
    return math.sqrt((l1[0]-l2[0])*(l1[0]-l2[0]) + (l1[1]-l2[1])*(l1[1]-l2[1]))

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split(','))))

s = list(itertools.combinations(l, 4))

lresult = []
for i in range(len(s)):
    li = list(s[i])
    li.sort()
    if isrectangle(li):
        lresult.append(areacalculate(li))

if len(lresult) == 0:
    print(0)
else:
    print('%.5f' % min(lresult))

#[[0,1],[2,1],[1,1],[1,0],[2,0]]

