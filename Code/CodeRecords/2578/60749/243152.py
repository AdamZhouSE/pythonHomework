nums=list(input())
threshould=int(input())
i=1
sum=0
while True:
    for x in nums:
        if x&i==0:
            sum+=x/i
        else:
            sum+=x//i+1
    if sum<=threshould:
        print(i)
        break
    i+=1

