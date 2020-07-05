piles = eval(input())
h = int(input())
l = min(piles)
r = max(piles)
while l<r:
    middle = (l+r)//2
    tmp = 0
    for i in piles:
        if i%middle==0:
            tmp += i//middle
        else:
            tmp += i//middle + 1
    if tmp>h:
        l = middle+1
    else:
        r = middle
print(l)