import re
num=int(input())
all=input().split(' ')
all=[int(x) for x in all]
def cal(all):
    temp=[]
    cons=[]
    for i in range(len(all)):
        temp.append(all[i])
        son(temp)
        cons.append(son(temp))
    return cons


def son(A):
    allA = []
    for i in range(len(A)):
        for k in range(i, len(A)):
            allA.append(A[i:k + 1])
    list2 = list(set([tuple(t) for t in allA]))
    return len(list2)
con=cal(all)
for k in con:
    print(k)