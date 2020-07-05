nums=[3,5,10]
tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    cs = []
    def constitude(sum):
        global nums,cs,n
        count=0
        for i in sum:
            count+=i
        if(count==n):
            list.sort(sum)
            if(sum not in cs):
                cs.append(sum)
        elif(count>n):
            return
        else:
            for i in nums:
                sum.append(i)
                constitude(list.copy(sum))
                sum=sum[:-1]
    constitude([])
    print(len(cs))