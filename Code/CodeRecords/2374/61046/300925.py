num=int(input())
length=[]
testList=[]
for i in range(num):
    length.append(input())
    testList.append(input())
for i in range(num):
    lst=testList[i].split()
    lst=list(map(int,lst))
    lst=sorted(lst)
    count={}
    for x in lst:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    newc=sorted(count.items(),key=lambda item:item[1],reverse=True)
    ans=''
    for key,value in newc:
        ans+=str(key)*value
    ans=list(ans)
    print(str(' '.join(ans))+' ')