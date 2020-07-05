string=input()
string.replace(' ','')
listt=string.split(",")
nums=[]
for n in listt:
    nums.append(int(n))
nums.sort()
        dp=[0 for x in range(len(nums))]
        index=[-1 for x in range(len(nums))]
        max_len,max_index=0,-1
        for i in range(len(nums)):
            dp[i]=1
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    index[i]=j
                if dp[i]>max_len:
                    max_len=dp[i]
                    max_index=i
        arr=[]
        while True:
            if max_index!=-1:
                arr.append(nums[max_index])
                max_index=index[max_index]
            else:
                break
        return arr[::-1]
————————————————
版权声明：本文为CSDN博主「_六六先森」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_37373020/article/details/81018538