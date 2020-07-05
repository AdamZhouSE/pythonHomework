def f(nums):
    sum=[0]
    for num in nums:
        sum.append(sum[-1]+num)
    return sum
sum=f(eval(input()))
lower=int(input())
upper=int(input())
cnt=0
for i in range(len(sum)-1):
    for j in range(i+1,len(sum)):
        ret=sum[j]-sum[i]
        if lower<=ret and ret<=upper: cnt+=1
print(cnt)