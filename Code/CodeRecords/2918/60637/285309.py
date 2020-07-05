n=(int)(input())
chest=list(map(int,input().strip().split(' ')))
list.sort(chest)
heap=1
weight=0
while(len(chest)>0):
    exist=False
    for i in range(len(chest)):
        if(chest[i]>=weight):
            del chest[i]
            exist=True
            weight+=1
            break
    if(not exist):
        heap+=1
        weight=0
print(heap)


