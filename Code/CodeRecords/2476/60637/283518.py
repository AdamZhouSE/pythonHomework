tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    arr=list(map(int,input().split(' ')))
    list.sort(arr)
    sum=0
    while(len(arr)!=1):
        temp=arr[0]+arr[1]
        sum+=temp
        arr=[temp]+arr[2:]
        list.sort(arr)
    print(sum)
