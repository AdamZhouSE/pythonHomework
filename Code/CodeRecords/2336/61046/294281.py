
num=int(input())
coutList=[]
testList=[]
for i in range(num):
    coutList.append(input())
    testList.append(input())

for i in range(num):
    q=coutList[i].split(" ")
    length=int(q[0])
    k=int(q[1])
    test=testList[i].split(" ")
    temp=[]
    res=[]
    c=0
    for n in range(length-k+1):
        for m in range(c,c+k):
            temp.append(test[m])
        f = list(map(int, temp))
        res.append(max(f))
        c+=1
        temp=[]
    end_str=""
    for x in res:
        end_str=end_str+str(x)+" "
    print(end_str)