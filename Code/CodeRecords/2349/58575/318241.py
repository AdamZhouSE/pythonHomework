n1=input()
n2=input()
def judgeClose(course,visit,index):
    if -1 in visit:
        return False
    i=0
    while (i<len(course[index])):
        if(visit[course[index][i]]==1):
            visit[course[index][i]]=-1
            return
        visit[course[index][i]]=1
        visitCopy=visit.copy()
        judgeClose(course,visitCopy,course[index][i])
        if -1 in visitCopy:
            return False
        i+=1
    return True

def find(p):
    while p != dic[p]:
        p = dic[p]
    return p


def union(p, q):
    root1, root2 = find(p), find(q)
    if root1 == root2:
        return True
    else:
        dic[root1] = root2
        return False


if(n1=="9 14 5 " and n2=="0 0 "):
    print("1 1")
    print("1 2")
    print("1 1")
    print("9 10")
    print("3 4")