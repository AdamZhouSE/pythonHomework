num=int(input())
nums=input().split(" ")
T=int(input())
ans=[]
for i in range(0,T):
    r=input().split(" ")
    l=int(r[0])-1
    r=int(r[1])
    temp=set(nums[l:r])
    print(len(temp))