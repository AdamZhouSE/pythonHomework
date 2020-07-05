total = int(input())
bisc = list(map(int,input().split(' ')))
sums = sum(bisc)
res = 0
for i in range(0,total):
    if (sums-bisc[i])%2 == 0:
        res+=1
print(res)