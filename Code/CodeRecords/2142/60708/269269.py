N=int(input())
for n in range(0,N):
    temp=input()
    list=[]
    listresult=[]
    k=-1#zhan
    t=-1#id
    for item in temp:
        if(item=='('):
            k=k+1
            t=t+1
            list.append(t)
            listresult.append(t)
        if(item==')'):
            listresult.append(list[k])
            list.pop(k)
            k=k-1
    for i in range(0,len(listresult)):
        print(listresult[i]+1,end=" ")
    print("")

