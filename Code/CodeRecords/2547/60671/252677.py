time=int(input())
while(time>0):
    time-=1
    length=int(input())
    strr=input()
    listt=strr.split()
    listnum=[]
    for x in listt:
        listnum.append(int(x))
    k=int(input())
    end=0
    for i in range(length-1):
        for j in range(i+1,length):
            if(abs(listnum[i]-listnum[j])==k):
                end+=1
    if(end==3):end=1
    if(end==4):end=2
    print(end)