def shiftUp(x):
    global heap
    t=(x-1)//2
    if heap[t]<heap[x]:
        tmp=heap[t]
        heap[t]=heap[x]
        heap[x]=tmp
        shiftUp(t)
    return

def shiftDown(x):
    global newheap
    global newnum
    l=x*2+1
    r=x*2+2
    if r<=newnum:
        selected=-1
        if newheap[l]<newheap[r]:
            selected=r
        else:
            selected=l
        if newheap[x]<newheap[selected]:
            tmp=newheap[x]
            newheap[x]=newheap[selected]
            newheap[selected]=tmp
            shiftdown(selected)
    elif l<=newnum:
        if newheap[x]<newheap[l]:
            tmp=newheap[x]
            newheap[x]=newheap[l]
            newheap[l]=tmp
            shiftdown(l)
    return

def query(n):
    global newheap
    global newnum
    global heap
    global num
    newheap=heap.copy()
    newnum=num
    for i in range(0,n):
        tmp=newheap[newnum-1]
        newheap[newnum-1]=newheap[0]
        newheap[0]=tmp
        newnum-=1
        shiftDown(0)
    print(newheap[newnum])
    return

def insert(x):
    global heap
    global num
    heap.append(x)
    num+=1
    shiftUp(num-1)
    return

m,q=map(int,input().split(' '))
gems=list(map(int,input().split(' ')))
heap=[]
newheap=[]
newnum=0
num=0
for gem in gems:
    insert(gem)
for i in range(0,q):
    operation,t=map(int,input().split(' '))
    if operation==1:
        query(t)
    else:
        insert(t)