nums=int(input())
for i in range(nums):
    [left,right]=list(map(int,input().split(" ")))
    count=0
    def isValid(num):
        tail=num%10
        while num>=10:
            num=num//10
        return num==tail
    for i in range(left,right+1):
        if isValid(i):
            count+=1
    print(count)