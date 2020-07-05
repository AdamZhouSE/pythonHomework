size=int(input())
for i in range(size):
    list0=input().split()
    m=int(list0[0])
    n=int(list0[1])
    list1=list(set(input().split()))
    list2=list(set(input().split()))
    count=0
    for k in range(len(list1)):
        for p in range(len(list2)):
            if list1[k]==list2[p]:
                count+=1
    print(count)