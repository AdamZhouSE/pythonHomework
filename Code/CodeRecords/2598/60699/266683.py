list1=list(map(int,input().split(' ')))
cnt=list1[0]
D=list1[1]
t=0
nums=[]
for i in range(0,cnt):
    opr=input().strip().split(' ')
    if len(opr)<=1:
        list3=[]
        list3.append(opr[0][0])
        list3.append(int(opr[0][1:]))
        opr=list3
    if opr[0]=='A':
        temp=t+int(opr[1])
        temp%=D
        nums.append(temp)
    else:
        res=-1000000000000000
        for j in range(max(0,len(nums)-int(opr[1])),len(nums)):
            res=max(res,nums[j])
        t=res
        print(res)
