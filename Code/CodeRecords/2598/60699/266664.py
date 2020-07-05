list1=list(map(int,input().split(' ')))
cnt=list1[0]
D=list1[1]
t=0
nums=[]
for i in range(0,cnt):
    opr=input().split(' ')
    if opr[0]=='A':
        t+=int(opr[1])
        t%=D
        nums.append(t)
    else:
        res=-1000000000000000
        for j in range(len(nums)-int(opr[1]),len(nums)):
            res=max(res,nums[j])
        t=res
        print(res)