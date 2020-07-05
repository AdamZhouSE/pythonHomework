N=int(input())
for n in range(0,N):
    temp=input()
    list=[]
    listresult=[]
    k=-1
    t=-1
    for item in temp:
        if(item=='('):
            list.append(item)
            k=k+1
            t=t+1
            listresult.append(t)
        if(item==')'):
            listresult.append(t)
            list.pop(k)
            k=k-1
    for i in range(0,len(listresult)):
        if i!=len(listresult)-1:
            print(listresult[i]+1,end=" ")
        else:
            print(listresult[i]+1)
