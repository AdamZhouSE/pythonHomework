n=int(input())
nums=[]
def func(nums,k):
    count=0
    for j in nums:
        if((j[0]*k+j[1])>j[2]):
            count+=1
    return count
mark=0
for i in range(0,n):
    s=input().split()
    if(s[0]=="Add"):
        t=list(map(int,s[1:]))
        nums.append(t)
    elif(s[0]=="Query"):
        k=int(s[1])
        print(func(nums,k))
    else:
        m=int(s[1])
        nums[m-1]=[0,0,0]
        
        
               