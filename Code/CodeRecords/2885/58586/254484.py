nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    temp=[c%3 for c in arr]
    sum=0
    sum+=temp.count(0)
    a=temp.count(1)
    b=temp.count(2)
    sum+=min(a,b)+(max(a,b)-min(a,b))//3
    print(sum)
