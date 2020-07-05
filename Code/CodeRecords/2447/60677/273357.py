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
line1=input().split()
line1=[int(x) for x in line1]
account=input().split()
account=[int(x) for x in account]
answer=[]
for i in range(line1[1]):
    temp=input().split()
    begin=int(temp[0])-1
    end=int(temp[1])
    heap=account[begin:end]
    buidUpHeap(heap,end-begin)
    answer.append(str(heap[0]))
print(" ".join(answer),end=" ")