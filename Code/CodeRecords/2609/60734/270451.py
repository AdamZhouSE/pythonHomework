def find_kth_single(lst,k):
    index = -1
    while k>0:
        index+=1
        if lst.count(lst[index]) == 1:
            k-=1
    return lst[index]
    
t = int(input())
for i in range(t):
    lst = list(map(int,input().split(' ')))
    n = lst[0]
    k = lst[1]
    lst = list(map(int,input().split(' ')))
    print(find_kth_single(lst,k))