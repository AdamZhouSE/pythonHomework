nums=list(map(int,input().split(",")))
k=int(input())
jud=False
for length in range(1,len(nums)+1):
    for start in range(0,len(nums)-length+1):
        sum=0
        for i in range(start,start+length):
            sum+=nums[i]
        if sum%k==0:
            jud=True
            break
    if jud:
        break
print(jud)