num=input().split(" ")
N=int(num[0])
M=int(num[1])
i=0
lis=[]
while(i<N):
    lis.append(False)
    i+=1
i=0
while(i<M):
    temp=input().split()
    temp=list(int(a) for a in temp)
    a = temp[1]
    b = temp[2]
    if(temp[0]==0):
        j=a-1;
        while(j<b):
            lis[j]=not lis[j]
            j+=1
    elif(temp[0]==1):
        j=a-1
        count=0;
        while(j<b):
            if(lis[j]):
                count+=1
            j+=1
        print(count)
    i+=1