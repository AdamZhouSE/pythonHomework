rb=input()
num_list=input().split()
nums=input().split()
res=[]
for i in num_list:
    if i in nums:
        res.append(i)
print(" ".join(res))