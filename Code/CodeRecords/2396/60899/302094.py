n = int(input())
list0 = list(map(int,input().split()))
for i in range(n):
    list2 = list0
    print(str(list0[i:].index(min(list0[i:]))+i+1)+" ",end="")
    tmp = list0[i:].index(min(list0[i:]))+i
    list1 = reversed(list0[i:tmp+1])
    list0 = list0[0:i]
    list0.extend(list1)
    if tmp != n-1:
        list0.extend(list2[tmp+1:])
    #print(list0)