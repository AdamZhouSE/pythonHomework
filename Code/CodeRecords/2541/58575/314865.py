n=int(input())
course=[[] for i in range(n)]
temp=input()[1:-1]

i=0
while(i<len(temp)):
    i=temp.index("[")
    j=temp.index("]")
    tmp=temp[i+1:j]
    tmp=list(map(int,tmp.split(",")))
    if tmp[1] not in course[tmp[0]]:
        course[tmp[0]].append(tmp[1])
    temp=temp[j+1:]
    i=j

res=[]
visit=[0 for i in range(n)]

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

i=0
judge=True
while(i<n and judge==True):
    visitCopy=visit.copy()
    visitCopy[i]=1
    judge=judgeClose(course,visitCopy,i)
    i+=1

if(judge==False):
    print([])
else:
    def calcu(course,index,res,m):
        if(len(course[index])==m or len(res)==m):
            return
        i = 0
        while (i < len(course[index])):
            if course[index][i] not in res:
                calcu(course, course[index][i],res,m-1)
                res.append(course[index][i])
            i += 1
        return

    i=0
    while(i<n):
        if(i in res):
            i+=1
            continue
        calcu(course,i,res,n)
        res.append(i)
        i+=1
    print(res)