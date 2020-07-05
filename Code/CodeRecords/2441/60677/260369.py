nums=input()[1:-1].split(",")
nums=[int(x) for x in nums]

def down(heap,i,length):
    if i>=length:
        return
    left=i*2
    right=i*2+1
    min=i
    if left<=length and heap[left-1]<heap[min-1]:
        min=left
    if right<=length and heap[right-1]<heap[min-1]:
        min=right
    if min!=i:
        tem=heap[min-1]
        heap[min-1]=heap[i-1]
        heap[i-1]=tem
        down(heap,min,length)

def buidUpHeap(heap,length):
    i=length//2
    while i!=0:
        down(heap,i,length)
        i-=1
buidUpHeap(nums,nums.__len__())

answer=[]
while nums.__len__()!=0:
    tem=nums[0]
    nums[0]=nums[nums.__len__()-1]
    nums[nums.__len__()-1]=tem
    answer.append(nums.pop(nums.__len__()-1))
    down(nums,1,nums.__len__())
print(answer)