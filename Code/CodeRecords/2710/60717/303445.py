tmp=input().split()
n=int(tmp[0])
q=int(tmp[1])
list1=[]
for i in range(0,q):
    tmp=input().split()
    if tmp[0]=='M':
        tmp1=[int(tmp[1]),int(tmp[2])]
        list1.append(tmp1)
        list1.sort()
    if tmp[0]=='D':
        index=0
        while True:
            if list1[index][0]>int(tmp[1]):
                break
            else:
                index+=1
        minn=n+1
        for i in range(0,index):
            if list1[i][1]>=int(tmp[2]):
                minn=min(minn,list1[i][1])
        if index==0 or minn==n+1:
            print(-1)
        else:
            print(minn)