def count_reverse(a):
    return a.count("0")-a.count("1")

length=int(input())
nums="".join(input().split())
max_reverse=0
for i in range(length):
    if(i=="1"):
        continue
    else:
        for j in range(i,length):
            max_reverse=max(max_reverse,count_reverse(nums[i:j]))
res=nums.count("1")+max_reverse
print(res)
            
    