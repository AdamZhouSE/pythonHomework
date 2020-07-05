nums=int(input())
for i in range(nums):
    num=int(input())
    if num>3 and num%3==0:
        ans=[num//3-1,num//3,num//3+1]
        print(*ans)
    else:
        print(-1)