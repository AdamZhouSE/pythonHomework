number=int(input())
lists=[]
length=[]
for i in range(number):
    source=[]
    num=int(input())
    length.append(num)
    lis=input().split(" ")
    for i in range(num):
        source.append(int(lis[i]))
    lists.append(source)
for i in range(len(lists)):
    ans=""
    lists[i].sort()
    for x in range(1,length[i]+1):
        if(lists[i].count(x)==2):
            ans=ans+str(x)+" "
            break
    if(ans==""):
        ans="0 "
    save=ans
    for x in range(1,length[i]+1):
        if(lists[i].count(x)==0):
            ans=ans+str(x)
            break
    if(ans==save):
        ans=ans+"0"
    print(ans)