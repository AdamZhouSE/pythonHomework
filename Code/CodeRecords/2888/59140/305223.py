temp = input().split(" ")
n, m = int(temp[0]), int(temp[1])
arr = [int(x) for x in input().split(" ")]
postive=arr.count(1)
negtive=arr.count(-1)
maxzero=min(postive,negtive)*2
for _ in range(m):
    temp = input().split(" ")
    l, r = int(temp[0]), int(temp[1])
    if (r-l+1)%2==1:print(0)
    else:
        if r-l+1<=maxzero:print(1)
        else:print(0)