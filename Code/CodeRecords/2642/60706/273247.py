str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
stones=[]
for i in range(len(list1)):
    stones.append(int(list1[i]))
n = len(stones)
ans=[]
if n <= 2:
    ans=[0, 0]
stones.sort()
max_moves = max(stones[n - 1] - stones[1] - n + 2,stones[n - 2] - stones[0] - n + 2)
min_moves = max_moves
ri = 0
for le in range(n):
    while ri + 1 < n and stones[ri + 1] - stones[le] + 1 <= n:
        ri += 1
    unoccupied = n - (ri - le + 1)
    if ri - le + 1 == n - 1 and stones[ri] - stones[le] + 1 == n - 1:
        unoccupied = 2
    min_moves = min(min_moves, unoccupied)
ans=[min_moves, max_moves]
print(ans)
