cases=int(input())
def queue1(src,std):
    cost=0
    for i in range(0,n-1):
        minindex=i
        minvalue=src[i]
        for j in range(i+1,n):
            if src[j]<minvalue:
                minvalue=src[j]
                minindex=j
        if i != minindex:
            tmp=src[minindex]
            del src[minindex]
            src.insert(i,tmp)
            cost+=1
        if src==std:
            break
    return cost
def queue2(src,std):
    cost = 0
    for i in range(n-1,-1,-1):
        maxindex = i
        maxvalue = src[i]
        for j in range(0, i):
            if src[j] > maxvalue:
                maxvalue = src[j]
                maxindex = j
        if i != maxindex:
            cost += 1
            tmp=src[maxindex]
            del src[maxindex]
            src.insert(i,tmp)
        if src == std:
            break
    return cost
for c in range(cases):
    n=int(input())
    students=[int(x) for x in input().split()]
    std=sorted(students)
    cost1=queue1(students[:],std)
    cost2=queue2(students[:],std)
    print(min(cost1,cost2))