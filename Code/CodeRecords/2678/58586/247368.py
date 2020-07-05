nums=int(input())
for i in range(nums):
    num=int(input())
    count=0
    pos=0
    ans=0
    while num>0:
        if num%2==1:
            count+=1
            ans=pos+1
        pos+=1
        num=num//2

    if count>1 or ans==0:
        print(-1)
    else:
        print(ans)