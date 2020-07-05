def trap(listp):    
    movepeak = 0
    triprain = 0
    maxindex = 0
    for i in range(1, len(listp)):
        if listp[i] > listp[maxindex]:
            maxindex = i
    for i in range(0, maxindex):
        if movepeak < listp[i]:
            movepeak = listp[i]
        else:
            triprain += movepeak - listp[i]
    movepeak = 0
    for j in range(len(listp) - 1, maxindex, -1):
        if movepeak < listp[j]:
            movepeak = listp[j]
        else:
            triprain += movepeak - listp[j]
    return triprain


t = int(input())
for ti in range(t):
    n = int(input())
    l = input().split(' ')
    li=[]
    for i in l:
        li.append(int(i))
    print(trap(li))