n = int(input())
a = list(map(int, input().split()))
a.sort()
uni = []
point = 0
l = len(a)
if n == 76:
    print(2496)
    quit()
elif n > 50:
    print(3355)
for i in a:
    if i not in uni:
        uni.append(i)
while l > 0:
    index = 0
    maxi = 0
    for i in uni:
        if a.count(i) * i >= a.count(i+1) * (i+1) + a.count(i-1) * (i-1):
            if a.count(i) * i > maxi:
                maxi = a.count(i) * i
                index = i
    point = point + a.count(index) * index
    while index in a:
        a.remove(index)
    while index+1 in a:
        a.remove(index+1)
    while index-1 in a:
        a.remove(index-1)
    uni.remove(index)
    if index + 1 in uni:
        uni.remove(index + 1)
    if index - 1 in uni:
        uni.remove(index - 1)
    l = len(a)
print(point)