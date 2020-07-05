nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    largest=0
    for j in arr:
        count=0
        if j-1 not in arr:
            temp=j
            while j in arr:
                count+=1
                j+=1
        largest=max(largest,count)
    print(largest)