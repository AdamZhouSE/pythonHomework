num=int(input())
testList=[]
count=0
rep=0
for i in range(num):
    testList.append(input())
for i in range(num):
    test=testList[i].split(" ")
    m=int(test[0])
    n=int(test[1])
    a=int(test[2])
    b=int(test[3])
    for i in range(m,n-1):
        if i%a==0 and i%b!=0:
            count+=1
        if i % a != 0 and i % b == 0:
            count += 1
        if i%a==0 and i%b==0:
            rep+=1
    print(count+rep)