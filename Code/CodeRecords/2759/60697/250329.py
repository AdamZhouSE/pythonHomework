t=int(input())
nums=[]
for i in range(t):
    nums.append(list(map(int,input().split(' '))))
for i in range(t):
    start=nums[i][0]
    end=nums[i][1]
    a=nums[i][2]
    b=nums[i][3]
    res=0
    for j in range(start,end+1):
        if(j%a==0):
            res+=1
        elif(j%b==0):
            res+=1
    print(res)