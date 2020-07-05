size=int(input())
for k in range(size):
    n=int(input())
    lst=[i+1 for i in range(n)]
    result=[0]*n
    base=1
    i=0
    count=1
    while(len(lst)>0):
        tmp=(i+base)%len(lst)
        i=(i+base)%len(lst)
        result[lst[tmp]-1] = count
        del lst[tmp]
        base+=1
        count+=1
    for i in range(len(result)-1):
        print(result[i],end=' ')
    print(result[-1])