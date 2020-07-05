n=(int)(input())
for index in range(n):
    A=input().split()
    B=input().split()
    n=(int)(A[1])
    now=[]
    for index in range(len(B)):
        now.append((int)(B[index]))


    index=0
    while index<len(now):
        if now[index]==-1:
            index+=1
        else:
            jishu=[]
            for index1 in range(index+1,len(now)):
                if now[index1]==now[index]:
                    jishu.append(index1)
            if jishu!=[]:
                now[index]=-1
                for i in jishu:
                    now[i]=-1
            index+=1
    count=0
    index=0
    while count<n and index<len(now):
        if now[index]!=-1:
            count+=1
            index+=1
        else:
            index+=1
    if index==len(now):
        print(-1)
    else:
        print(now[index-1])