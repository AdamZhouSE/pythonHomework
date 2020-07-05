n = list(map(int,input().split(',')))
loc = list(map(int,input().split(',')))
res = 0
left = loc[0]-n[0]
right = n[len(n)-1]-loc[len(loc)-1]
for i in range(0,len(loc)-1):
    if (loc[i+1]-loc[i]>res):
        res = loc[i+1]-loc[i]
res = int((res-1)/2)
if left >= right and left >= res:
    print(left)
elif right >= left and right >= res:
    print(right)
else:
    print(res)