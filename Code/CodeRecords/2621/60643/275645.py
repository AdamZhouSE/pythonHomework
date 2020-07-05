if __name__=="__main__":
    nums=input().split(",")
    nums=[int(x) for x in nums]
    ans=0
    sum=0
    for i in nums:
        sum+=i
        if sum<0:
            sum=0
        ans=max(sum,ans)
    print(ans)