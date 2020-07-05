n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
m=int(input())
for i in range(m):
    place=input().split(" ")
    left,right=int(place[0]),int(place[1])
    s=list(set(nums[left-1:right]))
    print(len(s))