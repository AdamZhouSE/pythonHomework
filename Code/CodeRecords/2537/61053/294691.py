def adjustHeap(heap):
    beg = int(len(heap)/2)-1
    while beg >= 0:
        adjust(heap,beg)
        beg -= 1

def adjust(heap:list,index):
    i = index
    child = 2 * i + 1
    while child < len(heap):
        #先定位到较大的子节点
        if child + 1 < len(heap) and heap[child + 1]>heap[child]:
            child += 1
        #然后与父节点进行比较
        if heap[child] > heap[i]:
            temp = heap[child]
            heap[child] = heap[i]
            heap[i] = temp

            i = child
            child = 2 * child + 1
        else:
            break



def find_k(numlst,k):
    heap = numlst[0:k]
    heap = sorted(heap,reverse = True)
    for i in range(k,len(numlst)):
        if numlst[i] > heap[k-1]:
            heap[k-1] = numlst[i]
            adjustHeap(heap)
    print(heap[k-1])

if __name__ == "__main__":
    numlst = eval(input())
    k = int(input())
    find_k(numlst,k)