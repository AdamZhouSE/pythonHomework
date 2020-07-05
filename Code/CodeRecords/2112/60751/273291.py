nums=input().split(",")
nums_=[]
for i in nums:
    nums_.append(int(i))
nums_.sort()
for i in range(len(nums_)):
    if i!=nums_[i]:
        print(i)
        break
