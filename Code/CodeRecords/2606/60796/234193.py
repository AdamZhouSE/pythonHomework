#注意：输入的是[-1,0,3,5,9,12]这样的字符串
nums=input()
target=input()
nums=nums[1:len(nums)]
ls=[]
ls=nums.split(",")
m=0
for i in range(0,len(ls)):
    if(target==ls[i]):
        print(i)
        m=1
        break
if (m==0):
    print(-1)

