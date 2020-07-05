time=int(input())
while(time>0):
    time-=1
    str0=input()
    list0=str0.split()
    string=list0[0]
    k=int(list0[1])
    listSub=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            listSub.append(string[i:j])
    fin=[]
    
    for item in listSub:
        count=0
        for o in listSub:
            if(item==o):
                count+=1
        if(count==k):
            fin.append(item)
    
    leng=[0]*100
    if(len(fin)==0):
        print(-1)
    else:
        for s in fin:
            leng[len(s)]+=1
        max0=0
        for i in leng:
            max0=max(max0,i)
        #print(leng.index(max0))