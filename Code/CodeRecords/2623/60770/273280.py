def solve():

    def percDown(hole,heap=[]):#heap[0]没有元素
        child=0
        tmp=heap[hole]
        currentSize=len(heap)-1
        while hole*2<=currentSize:
            child=hole*2
            if child!=currentSize:
                if heap[child+1]<heap[child]:
                    child+=1
            if heap[child]<tmp:
                heap[hole]=heap[child]
                hole=child
            else:
                break
        heap[hole]=tmp

    def buildHeap(arr=[]):#arr[0]没有元素，实际元素个数是len-1
        i=int((len(arr)-1)/2)
        while i>=1:
            percDown(i,arr)
            i-=1

    heap=[0]#[0]号位置无效
    nums=list(map(int,input().split(',')))
    k=int(input())
    heap+=nums[:k]
    buildHeap(heap)
    for i in range(k,len(nums)):
        if nums[i]>heap[1]:
            heap[1]=nums[i]
            percDown(1,heap)

    res=heap[1]
    print(res)

if  __name__ == '__main__' :
    solve()
