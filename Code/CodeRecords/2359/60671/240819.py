time=int(input())
while(time>0):
    length=int(input())
    str=input()
    list=str.split()
    listnum=[]
    for x in list:
        listnum.append(int(x))
    count=0
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if(listnum[i]+listnum[j]==listnum[k])or(listnum[i]+
                   listnum[k]==listnum[j])or(listnum[j]+listnum[k]==
                                             listnum[i]):
                    count+=1
    if(count!=0):
        print(count)
    else:
        print(-1)
    time-=1