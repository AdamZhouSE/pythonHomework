T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    lists=[]

    for x in temp:
        lists.append(int(x))

    start=-1
    end=-1
    res=[]
    for i in range(0,len(lists)-1):
        if lists[i+1]>lists[i] and start==-1:
            start=i
        if lists[i+1]<=lists[i] and start!=-1:
            end=i
        if start!=-1 and end!=-1:
            res.append("("+str(start)+" "+str(end)+")")
            start=-1
            end=-1

    if start!=-1:
        res.append("(" + str(start) + " " + str(len(lists)-1) + ")")

    for i in range(0,len(res)):
        print(res[i],end="")
        if i!=len(res)-1:
            print(" ",end="")
    print()