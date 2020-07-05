def find_valid_lst(m,n,arr):
    if len(arr) == n+1:
        valid_lsts.append(arr.copy())
        return
    
    if 2*arr[-1]>m:
        return
    for i in range(int(2*arr[-1]),m+1):
        arr.append(i)
        find_valid_lst(m,n,arr)
        arr.pop()

t = int(input())
for i in range(t):
    valid_lsts = []
    lst = list(map(int,input().split(' ')))
    m = lst[0]
    n = lst[1]
    find_valid_lst(m,n,[0.5])
    print(len(valid_lsts))