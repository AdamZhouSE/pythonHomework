def find_kth_min(a,k):
    a.sort()
    return a[k-1]
    
n, m = input().split(' ')
n, m = int(n), int(m)
lst = list(map(int,input().split(' ')))
for i in range(m):
    l, r, k = input().split(' ')
    l, r, k = int(l), int(r), int(k)
    print(find_kth_min(lst[l-1:r],k))