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
    # test=sorted(test)
    # for x in test:
    #     ans.append(int(x)*length)
    #     length-=1
    # print(max(ans))
    j=0
    for j in range(length-1):
        count = 1
        mid=test[j]
        for m in range(1,length-j):
            if int(mid)<=int(test[j+m]):
                count+=1

            else:
                break
        temp1.append(count)
    temp1.append(1)
    temp2.append(0)
    for j in range(1,length):
        count = 0
        mid=test[j]
        for m in range(1,j+1):
            if int(mid)<=int(test[j-m]):
                count+=1

            else:
                break
        temp2.append(count)
    for l in range(len(temp1)):
        temp.append(temp1[l]+temp2[l])
    k=0
    for x in test:
        ans.append(int(x)*temp[k])
        k+=1

    print(max(ans))