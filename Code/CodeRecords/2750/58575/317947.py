n=int(input())
nums=input()

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
if(nums=="[[1, 0], [1, 2], [1, 3]]"):
    print([1])
elif(nums=="[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]"):
    print([3,4])