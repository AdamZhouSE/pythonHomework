n = int(input())
meat = []
price = []
for i in range(0, n):
    mp = input().split(" ")
    meat.append(int(mp[0]))
    price.append(int(mp[1]))
i = 1
pr = 0
sump = 0
summ = meat[pr]
while pr + i < n:
    if price[pr+i] >= price[pr]:
        sump += price[pr] * summ
        summ = meat[pr+i]
        i += 1
        if pr + i == n:
            sump += price[pr]*summ
    else:
        sump += price[pr] * summ
        pr = pr + i
        i = 1
        summ = meat[pr]
        if pr == n-1:
            sump += price[pr]*summ
print(sump)