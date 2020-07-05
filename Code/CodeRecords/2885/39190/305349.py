def func17(arr):
    count0=count1=count2=0
    for i in range(len(arr)):
        if int(arr[i])%3==0:
            count0=count0+1
        elif int(arr[i])%3==1:
            count1=count1+1
        else:
            count2=count2+1
    count=count0
    tmp=min(count1,count2)
    count=count+tmp+int((count1-tmp-(count1-tmp)%3)/3)+int((count2-tmp-(count2-tmp)%3)/3)
    print(count)
    
tests=int(input())
for i in range(tests):
    input()
    arr=input().split(" ")
    func17(arr)
    