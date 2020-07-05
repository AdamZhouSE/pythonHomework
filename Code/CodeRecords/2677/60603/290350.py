testnum=int(input())
for i in range(testnum):
    num=int(input())
    list=input().split(" ")
    count=0
    for j in range(num):
        list[j]=int(list[j])
    for j in range(num):
        for m in range(j+1,num):
            if(list[j]^list[m]==0):
                count+=1
    print(count)
