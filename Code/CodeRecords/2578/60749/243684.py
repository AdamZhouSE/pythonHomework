nums=input()
threshould=int(input())
i=1
sum=0
while True:
    for x in  range(0,len(nums)):
        if nums[x]%i==0:
            sum+=nums[x]/i
        else:
            sum+=nums[x]//i+1
    if sum<=threshould:
        print(i)
        break
    sum=0
    i+=1



