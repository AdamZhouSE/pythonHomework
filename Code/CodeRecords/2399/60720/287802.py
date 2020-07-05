size=int(input())
def mul(num):
    result=1
    while(num>1):
        result*=num
        num-=1
    return result
for k in range(size):
    lst=input().split()
    lst=list(map(int,lst))
    n=lst[0]
    m=lst[1]
    l=lst[2]
    r=lst[3]
    list1=input().split()
    list1=list(map(int,list1))
    list1.sort()
    toA=[]
    for i in range(l,r+1):
        list2=[list1.count(i),i]
        toA.append(list2)
    toA.sort()
    i=0
    count=0
    isF=False
    if len(toA)==1:
        for i in range(m):
            list1.append(l)
    else:
        while(count<m):
            if i==len(toA)-1:
                for j in range(i+1):
                    if count==m:
                        isF=True
                        break
                    toA[j][0] += 1
                    count+=1
                    list1.append(toA[j][1])
                i=0
            if isF:
                break
            if toA[i][0]<toA[i+1][0]:
                toA[i][0]+=1
                list1.append(toA[i][1])
                count+=1
                for j in range(i):
                    if count==m:
                        isF=True
                        break
                    toA[j][0]+=1
                    list1.append(toA[j][1])
                    count+=1
            else:
                i+=1
            if isF:
                break
    list1.sort()
    base=mul(len(list1))
    count=1
    for i in range(len(list1)-1):
        if list1[i+1]==list1[i]:
            count+=1
        else:
            if count!=1:
                base//=mul(count)
                count=1
    if count!=1:
        base//=mul(count)
    print(base)