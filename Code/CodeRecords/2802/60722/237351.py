string=input().split(" ")
n=int(string[0])
m=int(string[1])
nums=input().split(" ")
seq=[]
for i in range(n):
    nums[i]=int(nums[i])
    seq.append(i+1)
while len(nums)!=1:
    if nums[0]<=m:
        del nums[0]
        del seq[0]
    else:
        nums.append(nums[0]-m)
        seq.append(seq[0])
        del nums[0]
        del seq[0]
print(seq[0])