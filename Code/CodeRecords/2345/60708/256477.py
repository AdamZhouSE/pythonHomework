N=eval(input())
for n in range(0,N):
    l=eval(input())
    listwrong=input().split(" ")
    listresult=[]
    listright=[]
    for i in range(0,l):
        listright.append(str(i+1))
    for i in range(0,l-1):
        if listwrong[i]==listwrong[i+1]:
            listresult.append(listwrong[i])
            break
    if len(listresult)!=1:
        listresult.append("0")
    for i in range(0,l):
        if listright[i]!=listwrong[i]:
            listresult.append(listright[i])
            break
    if len(listresult)!=2:
        listresult.append("0")
    for j,item in enumerate(listresult):
        if j!=len(listresult)-1:
            print(item,end=" ")
        else:
            print(item,end="")

    print("")