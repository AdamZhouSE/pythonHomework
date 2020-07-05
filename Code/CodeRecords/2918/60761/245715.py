def leastHeap(boxes):#传入已排好序的数组
    i=len(boxes)-1
    while(i>0):
        if (sum(boxes[i:])>=i):
            return max(leastHeap(boxes[:i]),len(boxes)-i)
        i=i-1
    return len(boxes)

n=int(input(""))
boxes=list(map(int,input().split(" ")))
boxes.sort()
print(leastHeap(boxes))