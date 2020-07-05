n=int(input())
box=list(map(int,input().split()))
box.sort()
out=0
heap=[]
out=0
while(len(box)>0):
    for i in range(0,len(box)):
        if(box[i]>=len(heap)):
            heap.append(box[i])
    if(i==len(box)-1):
        out+=1
        for j in heap:
            box.remove(j)
        heap=[]
print(out)