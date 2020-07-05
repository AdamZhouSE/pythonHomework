n = int(input())
lst = list(map(int,input().split(' ')))
boxes = []
piles = []
for x in lst:
    boxes.append([1,x])
boxes = sorted(boxes,key = lambda x:x[1])
while len(boxes)>0:
    first = boxes.pop(0)
    index = 0
    #找到第一个满足要求的盒子
    while index<len(boxes):
        if boxes[index][1]>=first[0]:
            boxes.insert(0,[1+first[0],boxes.pop(index)[1]-first[0]])
            break
        else:
            index+=1
    if index == len(boxes) or len(boxes) == 0:
        piles.append(first)
print(len(piles))