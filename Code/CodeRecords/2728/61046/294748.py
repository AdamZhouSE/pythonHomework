num=int(input())
numlist=[]
testList=[]
for i in range(num):
    numlist.append(input())
    testList.append(input())
for i in range(num):
    ans=[]
    temp1=[]
    temp2=[]
    temp=[]
    length=int(numlist[i])
    test=testList[i].split(" ")
    ss=0
    for x in test:
        if x=="":
            ss+=1
    
    for i in range(ss):
        test.remove("")
    
    test=list(map(int,test))

    j=0
    for j in range(length):
        count = length-1-j
        mid=test[j]
        for m in range(1,length-j):
            if mid < test[length - m]:
                break
            if mid>=test[length-m]:
                count-=1
        temp1.append(count)
    k=0
    for x in test:
        ans.append(x*temp1[k])
        k += 1

    test1=test[::-1]
    j = 0
    for j in range(length):
        count = length - 1 - j
        mid = test1[j]
        for m in range(1, length - j):
            if mid < test1[length - m]:
                break
            if mid >= test1[length - m]:
                count -= 1
        temp2.append(count)
    k = 0
    for x in test1:
        ans.append(x * temp2[k])
        k += 1
    print(max(ans))