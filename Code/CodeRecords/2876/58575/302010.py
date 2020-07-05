num=int(input())
nums=input().split(" ")
i=1
times=0
while i<num-1:
    if nums[i]=='0' and nums[i-1]=='1' and nums[i+1]=='1':
        times+=1
        nums[i+1]='0'
    i=i+1
print(times)