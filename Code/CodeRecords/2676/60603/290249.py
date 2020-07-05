testnum=int(input())
for i in range(testnum):
    ans=0
    string=input().split(" ")
    num=int(string[0])
    length=int(string[1])
    list=input().split(" ")
    for j in range(num):
        list[j]=int(list[j])

    for j in range(0,num-length+1):
        count=0
        for m in range(0,length):
            count+=list[j+m]
        if(count>ans):
            ans=count

    print(ans)