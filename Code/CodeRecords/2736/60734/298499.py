import re
def find_kth_min(a,k):
    a.sort()
    return a[k-1]

n, m = input().split(' ')
n, m = int(n), int(m)
lst = list(map(int,re.findall(r'\d+',input())))
for i in range(m):
    step = input().split(' ')
    if step[0] == 'Q':
        l,r,k = int(step[1]), int(step[2]), int(step[3])
        print(find_kth_min(lst[l-1:r],k))
    elif step[0] == 'C':
        x, y = int(step[1]), int(step[2])
        lst[x-1] = y