nums=list(map(int,input().strip("[").strip("]").split(",")))
def reverse(nums):
    l=[]
    for i in range(len(nums)):
        l.append(nums[-1-i])
    return l

def find_max(nums):
    index=0
    max_=0
    for i in range(len(nums)):
        if nums[i]>max_:
            max_=nums[i]
            index=i
    return index

sequence=[]
for i in range(0,len(nums)-1):
    index=find_max(nums[:len(nums)-i])
    if(index!=0):
        sequence.append(index+1)
        if nums==sorted(nums):
            break
    sequence.append(len(nums)-i)
    if nums == sorted(nums):
        break
#print(nums)
print(sequence)