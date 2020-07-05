nums=input()
threshould=int(input())
i=1
sum=0
def minimum(nums):
    i=1
    sum=0
    
    while True:
        
        if nums % i == 0:
            sum += nums[x] / i
        else:
            sum += nums[x] // i + 1
        if sum <= threshould:
            return i
            
        sum = 0
        i += 1
        
        
while True:
    if nums is int:
        print(minimum(nums))
        break
        
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


