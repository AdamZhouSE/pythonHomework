
def isSubString(s1, s2):
    if len(s1) > len(s2):
        return False
    tot = 0
    for i in list(s2):
        if tot == len(s1): break
        if i == s1[tot]:
            tot+=1
    return tot == len(s1)

def showDupSubString(s):
    s = list(s)
    li = []
    templi = []
    lastTemp = None
    for i in s:
        if lastTemp != i:
            if len(templi) > 1:
                li.append(templi.copy())
            lastTemp = i
            templi = [i]
        else:
            templi.append(i)
    if len(templi) > 1:
        li.append(templi)
    return li


def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().strip())
        t.append(input().strip())

    for i in range(n):
        ss = s[i]
        tt = t[i]
        # print(showDupSubString(ss))
        # print(showDupSubString(tt))
        if isSubString(ss,tt) and showDupSubString(ss) == showDupSubString(tt):
            print("YES")
        else: print("NO")

if __name__ == '__main__':
    solve()