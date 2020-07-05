n=int(input())
nums=list(map(int,input().split(" ")))
deleteNumber=0
i=len(nums)-1
while i>=5:
    if nums[i]==42:
        judge=False
        j=i-1
        while j>=4 and judge==False:
            if nums[j]==23:
                k=j-1
                while k>=3 and judge==False:
                    if nums[k]==16:
                        l=k-1
                        while l>=2 and judge==False:
                            if nums[l]==15:
                                m=l-1
                                while m>=1 and judge==False:
                                    if nums[m]==8:
                                        t=m-1
                                        while t>=0 and judge==False:
                                            if nums[t]==4:
                                                nums=nums[0:t]+nums[t+1:m]+nums[m+1:l]+nums[l+1:k]+nums[k+1:j]+nums[j+1:i]
                                                judge=True
                                            t-=1
                                    m-=1
                            l-=1
                    k-=1
            j-=1
        if judge==False:
            deleteNumber+=1
            nums=nums[0:-1]

    else:
        deleteNumber+=1
        nums=nums[0:-1]
    i=len(nums)-1
deleteNumber+=len(nums)
print(deleteNumber)
