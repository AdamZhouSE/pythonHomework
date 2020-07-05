UCs=int(input())
for UC in range(UCs):
    rb=input()
    nums=list(map(int,input().split()))
    if(sum(nums)%3==0):
        print(1)
    else:
        print(0)